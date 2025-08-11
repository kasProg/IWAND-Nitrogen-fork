
'''
Users can expand IWAND-Nitrogen by extracting additional attributes from the NHDPlus Selected Attributes V2.1 dataset.
The example function below demonstrates how to:

1. Read an attribute table that includes at least the gauge name and snapped COMID, such as the Basin_Attributes.csv file provided in the IWAND-Nitrogen dataset.

2. Download an attribute table from the NHDPlus Selected Attributes V2.1 dataset:
https://www.usgs.gov/data/attributes-nhdplus-version-21-catchments-and-modified-routing-upstream-watersheds-selected
Here, we use estimated nitrogen from septic systems for the reach catchments as an example.

3. Extract the attribute of interest.
'''
import pandas as pd
import geopandas as gpd
import os
os.chdir("./data/")

def get_nhdplus(att_p, nhd_p, columns):
    #read gauge file
    df0=pd.read_csv(att_p)
    
    #read nhdplus selected attributes file
    df1=pd.read_csv(nhd_p)
    df1=df1[["COMID",columns]]
    df0 = pd.merge(
        df0,         
        df1,         
        on='COMID',   
        how='left',
        
    )
    return(df0)


att_p="./IWAND-Nitrogen/Basin_Attributes.csv"
nhd_p="./NHDPlus_atts/Nsep2010.txt"
basin_att = get_nhdplus( att_p,nhd_p, "NSEP2010" )  