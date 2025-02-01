import dagster as dg
import pyarrow as pa
from dagster import Definitions
from dagster_duckdb import DuckDBResource
from dagster_gcp import BigQueryResource


@dg.asset
def hello(context: dg.AssetExecutionContext):
    context.log.info("Hello!")


@dg.asset(deps=[hello])
def world(
    context: dg.AssetExecutionContext,
    bigquery: BigQueryResource,
    duckdb: DuckDBResource,
):
    with bigquery.get_client() as bq_client, duckdb.get_connection() as get_client:
        query = "SELECT * from `opensource-observer.oso.stg_passport__scores`"
        job = bq_client.query(query)
        result: pa.Table = job.to_arrow(create_bqstorage_client=True)  # noqa: F841

        get_client.execute(
            """
            create or replace table passport_scores as (
                select * from result
            )
            """
        )


defs = dg.Definitions(assets=[hello, world])


defs = Definitions(
    assets=[hello, world],
    resources={
        "bigquery": BigQueryResource(
            project=dg.EnvVar("BIGQUERY_PROJECT"),
        ),
        "duckdb": DuckDBResource(database="data/database.duckdb"),
    },
)
