import dagster as dg
import pyarrow as pa
from dagster import Definitions
from dagster_duckdb import DuckDBResource
from dagster_gcp import BigQueryResource


@dg.asset
def hello(context: dg.AssetExecutionContext):
    context.log.info("Hello!")


@dg.asset
def collections(
    context: dg.AssetExecutionContext,
    bigquery: BigQueryResource,
    duckdb: DuckDBResource,
):
    with bigquery.get_client() as bq_client, duckdb.get_connection() as duckdb_client:
        query = """
            select * from `opensource-observer.oso.collections_v1`
        """
        job = bq_client.query(query)
        result: pa.Table = job.to_arrow(create_bqstorage_client=True)

        context.log.info(result.column_names)

        duckdb_client.execute(
            """
            create or replace table collections as (
                select * from result
            )
        """
        )


@dg.asset(deps=[hello])
def world(
    context: dg.AssetExecutionContext,
    bigquery: BigQueryResource,
    duckdb: DuckDBResource,
):
    with bigquery.get_client() as bq_client, duckdb.get_connection() as get_client:
        query = "SELECT * from `opensource-observer.oso.stg_passport__scores`"
        job = bq_client.query(query)
        result: pa.Table = job.to_arrow(create_bqstorage_client=True)

        context.log.info(result.column_names)

        get_client.execute(
            """
            create or replace table passport_scores as (
                select * from result
            )
            """
        )

        context.log.info("World!")


defs = Definitions(
    assets=[hello, world, collections],
    resources={
        "bigquery": BigQueryResource(
            project=dg.EnvVar("BIGQUERY_PROJECT"),
            gcp_credentials=dg.EnvVar("ENCODED_GOOGLE_APPLICATION_CREDENTIALS"),
        ),
        "duckdb": DuckDBResource(database="data/database.duckdb"),
    },
)
