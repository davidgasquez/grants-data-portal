import dagster as dg


@dg.asset
def my_asset(context: dg.AssetExecutionContext) -> dg.MaterializeResult:
    context.log.info("Hello, world!")
    return dg.MaterializeResult(
        metadata={"hello": "world"},
    )
