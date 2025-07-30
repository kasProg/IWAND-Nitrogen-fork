'''
Users can expand IWAND-Nitrogen by extracting additional forcings or applying the workflow to new watersheds. The function below demonstrates how to:
1. Read a watershed shapefile.
2. Reproject to the correct coordinate system as needed.
3. Compute zonal statistics (e.g., mean) of any raster forcing dataset.
4. Export a dataframe with watershed attributes and basin-averaged forcing values.
'''
import pandas as pd
import geopandas as gpd
from rasterstats import zonal_stats

def extract_watershed_stats(watershed_path, raster_path, var_name, save_path=None):

    # Load watershed boundaries
    wshd = gpd.read_file(watershed_path)

    # Get raster CRS
    with rasterio.open(raster_path) as src:
        raster_crs = src.crs

    if wshd.crs is None:
        raise ValueError("Watershed file has no CRS defined. Please define a CRS before running.")
    
    # Reproject watershed to raster CRS if needed
    if wshd.crs != raster_crs:
        wshd = wshd.to_crs(raster_crs)

    # Prepare base dataframe without geometry
    df_wshd = wshd.drop(columns=["geometry"])
    
    # Compute zonal statistics (mean values for each watershed polygon)
    stats = zonal_stats(wshd, raster_path, stats="mean")
    stats_df = pd.DataFrame(stats)
    
    # Add forcing variable to dataframe
    df_wshd[var_name] = stats_df["mean"].values
    
    # Optionally save results
    if save_path:
        df_wshd.to_csv(save_path, index=False)
    
    return df_wshd

