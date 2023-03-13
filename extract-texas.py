import geopandas as gpd

# Import tl_2022_us_state.json from data folder
states = gpd.read_file("data/tl_2022_us_state.json")

# Filter for Texas
texas = states[states["NAME"] == "Texas"]

# Export to geojson
texas.to_file("output/texas.geojson", driver="GeoJSON")