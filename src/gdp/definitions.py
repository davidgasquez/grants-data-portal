from dagster.components import definitions, load_defs

import gdp.defs


@definitions
def defs():
    return load_defs(defs_root=gdp.defs)
