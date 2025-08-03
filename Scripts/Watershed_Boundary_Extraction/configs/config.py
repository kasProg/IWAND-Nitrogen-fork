
# Define the list of HUCs
HUC_no_lst = ['01','02','03','04','05',
              '06','07','08','09','10',
              '11','12','13','14',
              '16','17','18']

#Define the required fields
required_fields = ["COMID", "Monitoring", "lat","lon" , "AreaSqKM", "wshd area", "TotDASqKM", "Source", "GII", "WT"]

# Define the groups dictionary
categories_dict = {   1: 'gII_name',
                      2: 'SWT_name',
                      3: 'gII_snap',
                      4: 'SWT_snap',
                      5: 'autodel'
                  }

# Define paths
# Shapefiles for the Watershed boundaries for study sites of the U.S. Geological Survey Surface Water Trends projectcan be downloaded at  # https://data.usgs.gov/datacatalog/data/USGS:57a9e239e4b05e859be05534
SWTrends_path       = "path to shape files from Watershed boundaries for study sites of the U.S. Geological Survey Surface Water Trends project"

# Path to all gauges/ csv files for different HUCs. (An example dataset can be found in the project folder /data/HUC02/csv/)
Huc_csv_path        = r"./data/HUC_{}/csv"

# Path to save all the output shapefiles for the watershed boundaries
output_path         = r"./data/HUC_{}/output_shapefiles"

# Path to csv files produced from running the Rcode "get_UTcomids.R" located in the project folder /Scripts/Watershed_Boundary_Extraction/Rcodes/ to get the upstream COMIDs for each gauge 
UScomids_path       = r"./data/HUC_{}/gauges_UScomids"

# Path to the catchment shapefiles for all HUCs provided by NHDPlus at https://www.epa.gov/waterdata/get-nhdplus-national-hydrography-dataset-plus-data#Download 
catchment_path      = r"path to NHDPlusCatchment shapefiles for all HUCs from NHDPlus"

# Path to the watershed boundaries shapefiles for all gauges in GAGES-II  dataset provided at https://data.usgs.gov/datacatalog/data/USGS:1d623649-ccb9-4238-8add-3174bc322fdf
input_gaugesII_path = r"path to shape files from GAGES-II: Geospatial Attributes of Gages for Evaluating Streamflow by USGS" 





