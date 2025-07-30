
# Define the list of HUCs
HUC_no_lst = ['01','02','03','04','05',
              '06','07','08','09','10',
              '11','12','13','14',
              '16','17','18']

#Define the required fields
required_fields = ["COMID", "Monitoring","lat","lon", "AreaSqKM","wshd area","TotDASqKM", "Source", "GII", "WT"]

# Define the groups dictionary
categories_dict = {   1: 'gII_name',
                      2: 'SWT_name',
                      3: 'gII_snap',
                      4: 'SWT_snap',
                      5: 'autodel'
                  }

# Define paths
SWTrends_path       = "path to shape files from Watershed boundaries for study sites of the U.S. Geological Survey Surface Water Trends project" #https://data.usgs.gov/datacatalog/data/USGS:57a9e239e4b05e859be05534
Huc_csv_path        = r".\data\HUC_{}\csv"
output_path         = r".\data\HUC_{}\output_shapefiles"
UScomids_path       = r".\data\HUC_{}\gauges_UScomids"
catchment_path      = r"path to NHDPlusCatchment for all HUCs from NHDPlus"
input_gaugesII_path = r"path to shape files from GAGES-II: Geospatial Attributes of Gages for Evaluating Streamflow by USGS" #https://data.usgs.gov/datacatalog/data/USGS:1d623649-ccb9-4238-8add-3174bc322fdf


