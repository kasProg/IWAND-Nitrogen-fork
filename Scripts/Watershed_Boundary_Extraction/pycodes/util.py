import geopandas as gpd
import os
import glob
import numpy as np
import pandas as pd
import shutil

class extract_watershedboundary():
    def __init__(self, SWTrends_path, input_gagesII_path, catchment_path, Huc_csv_path, UScomids_path, output_path):
        # initialize all the required paths
        self.Huc_csv_path   = Huc_csv_path
        self.UScomids_path  = UScomids_path
        self.output_path    = output_path
        self.catchment_path = catchment_path
        self.SWTrends_path  = SWTrends_path
        self.input_gagesII_path = input_gagesII_path

        # read the shape files from Watershed boundaries for study sites of the U.S. Geological Survey Surface Water Trends project
        self.SWTrends_shp  = gpd.read_file(os.path.join(self.SWTrends_path, "SW-Trends-watershed-bounds-shapefile\SWTrends_watershed_boundaries.shp"))
        self.df_SWTrends   =  pd.read_csv(os.path.join(self.SWTrends_path, "SWTrends_watershed_boundaries.txt"))

        # read the paths to shape files from GAGES-II: Geospatial Attributes of Gages for Evaluating Streamflow by USGS
        self.files_gageII       = os.listdir(self.input_gagesII_path)

    def extract_gII_gauges(self, file_in, file_out, Huc_no, name= True):
        # Description: A function to extract watershed boundary files for gauges in common with GAGES-II based on name query or COMID query
        
        # Input:
        # - file_in : input csv file (ex: "/data/HUC{Huc_no}/csv/gauges_gII_name_{Huc_no}.csv" or "/data/HUC{Huc_no}/csv/gauges_gII_snap_{Huc_no}.csv")
        # - file_out: output csv file (same as input file with area_src column added, area_src is the area of the gauge watershed boundary shapefile)
        # - Huc_no  : is the number of current HUC working on from HUC_list
        # - name    : a boolean flag if true > working on gauges found by name query, else > working on gauges found by COMID query

        df_common_gages = pd.read_csv(os.path.join(self.Huc_csv_path.format(Huc_no), file_in), dtype={'GII': str, 'WT': str})
        monitoring_lst  = df_common_gages['Monitoring'].values.tolist()
        GII_lst         = df_common_gages['GII'].values.tolist()
        area_src_lst    = []
        for gage, match in zip(monitoring_lst, GII_lst):
            # gauges in common with GAGES-II based on name query 
            if name:
                gage_id = gage[5:] if "USGS" in gage else gage
            else:
            # gauges in common with GAGES-II based on COMID query  
                gage_id = match[:-2] if Huc_no == '09' else match #HUC = 09
            gage_files = glob.glob(os.path.join(self.input_gagesII_path,f'*{gage_id}*'))
            gage_shp_file = gpd.read_file([path for path in gage_files if path.endswith('.shp')][0])
            area_src_lst.append(gage_shp_file['AREA'].values.item()/10**6) # convert from square meters to square kilometres

            # Loop through the matching files and copy them to the destination directory
            gage_name = gage
            for file_path in gage_files:
                # Get the base file name (without the path)
                file_name = os.path.basename(file_path)
                if "/" in gage_name:
                    gage_name = gage_name.replace("/", "")
                    print("gage name is replaced with ", gage_name)
                file_name = file_name.replace(file_name[8:-4], gage_name)#[5:] if "USGS" in gage else gage

                # Construct the destination file path
                destination_path = os.path.join(self.output_path.format(Huc_no), "gages_II",file_name)

                # Copy the file to the destination directory
                shutil.copy(file_path, destination_path)

        # Add the area source column (area of the gauges watershed boundary file) to the HUC csv file
        df_common_gages['area_src'] = area_src_lst
        df_common_gages.to_csv((os.path.join(self.Huc_csv_path.format(Huc_no), "check/", file_out)), index = False)
        return 


    def extract_SWTrends_gauges(self, file_in, file_out, Huc_no,name = True):
        # Description: A function to extract watershed boundary files for gauges in common with SWTrends dataset based on name query or COMID query
        
        # Input:
        # - file_in : input csv file (ex: "/data/HUC{Huc_no}/csv/gauges_SWT_name_{Huc_no}.csv" or "/data/HUC{Huc_no}/csv/gauges_SWT_snap_{Huc_no}.csv")
        # - file_out: output csv file (same as input file with area_src column added, area_src is the area of the gauge watershed boundary shapefile)
        # - Huc_no  : is the number of current HUC working on from HUC_list
        # - name    : a boolean flag if true > working on gauges found by name query, else > working on gauges found by COMID query
        df_common_gages = pd.read_csv(os.path.join(self.Huc_csv_path.format(Huc_no), file_in), dtype={'GII': str, 'WT': str})

        # Add other fields required for the validation of the extracted watershed boundary files
        area_src_lst      = []
        comid_src_lst     = []
        
        # Create a list with all the gauges in the csv file
        gages_lst_common = df_common_gages['Monitoring'].values.tolist()
        WT_data_lst      = df_common_gages['WT'].values.tolist()
        
        # loop through the gauges and extract the area and the COMID for each gauge
        for gage, WT in zip(gages_lst_common, WT_data_lst):
            if name:
                gage_id = gage[5:] if 'USGS' in gage else gage
            else:
                gage_id = WT[:-2] if Huc_no == '16' else WT

            comid_src_lst.append( self.df_SWTrends .loc[ self.df_SWTrends ['BasinID'] == gage_id,'ComID'].item())
            area_src_lst.append( self.df_SWTrends .loc[ self.df_SWTrends ['BasinID'] == gage_id,'gisareakm2'].item()) 
            id_record = self.SWTrends_shp[self.SWTrends_shp['BasinID'] == gage_id]

            gage_name = gage
            if "/" in gage_name:
                gage_name = gage_name.replace("/", "")
                print ("gage name is replaced with ", gage_name)
            filename = "GAGE_ID_" + str(gage_name)

            id_record.to_file(os.path.join(self.output_path.format(Huc_no),"WaterTrends",f"{filename}.shp"))

        df_common_gages['COMID_src'] = comid_src_lst
        df_common_gages['area_src']  = area_src_lst

        # Add the area source column (area of the gauges watershed boundary file) to the HUC csv file
        df_common_gages.to_csv(os.path.join(self.Huc_csv_path.format(Huc_no), "check/",file_out), index = False)
        return

    def auto_delineate_gauges(self, file_in, file_out, Huc_no):
        # Description: A function to extract watershed boundary files for gauges not found in common with GAGES-II or SWTrends dataset
        
        # Input:
        # - file_in : input csv file (ex: "/data/HUC{Huc_no}/csv/gauges_autodel_{Huc_no}.csv")
        # - file_out: output csv file (same as input file with area_src column added, area_src is the area of the gauge watershed boundary shapefile)
        # - Huc_no  : is the number of current HUC working on from HUC_list

        gages_files   = os.listdir(self.UScomids_path.format(Huc_no))
        catchment_shp = gpd.read_file(os.path.join(self.catchment_path.format(Huc_no), "Catchment.shp"))
        df_gages      = pd.read_csv(os.path.join(self.Huc_csv_path.format(Huc_no),file_in), dtype={'GII': str, 'WT': str})

        # Initialize grouping for QA/QC check
        group_lst           = ['group A', 'group B', 'group C', 'group D']
        df_gages[group_lst] = np.nan;

        # loop through each gauge in Group V
        for file in gages_files:
            df_gage = pd.read_csv(os.path.join(self.UScomids_path.format(Huc_no), file))

            gage_id    = file[5:-13] if 'USGS' in file else file[:-13]
            gage_fulnm = file[:-13]

            print(gage_id)

            gage_UTcomids = df_gage['COMID'].values.tolist()
            df_common     = catchment_shp[catchment_shp['FEATUREID'].isin(gage_UTcomids)]
            df_common     = df_common.to_crs(crs=3857)
            df_common['geometry'] = df_common['geometry'].buffer(0.000001)
            df_common     = df_common.to_crs(crs=catchment_shp.crs)
            df_common     = df_common[['AreaSqKM', 'geometry']]
            df_common['gage_id'] = gage_id
            df_common     = df_common.dissolve(by='gage_id', aggfunc='sum')
            df_common['gage_id'] = df_common.index
            df_common     = df_common.reset_index(drop=True)

            if df_common.shape[0] == 0:
                df_gages.loc[df_gages['Monitoring'] == gage_fulnm, 'Area_agg'] = "NOT FOUND"
                group = 'group C'

            else:
                df_gages.loc[df_gages['Monitoring'] == gage_fulnm, 'Area_agg'] = df_common.AreaSqKM.values
                # Run QAQC check
                
                # Ground truth area for the gauge watershed area: convert from square miles to square kilometres
                obs_area  = df_gages.loc[df_gages['Monitoring'] == gage_fulnm, 'wshd area'].item() * 2.58999 
                
                # Total drainage area in square kilometres corresponding to a specific COMID extracted from NHDPlus dataset
                comid_area= df_gages.loc[df_gages['Monitoring'] == gage_fulnm, 'TotDASqKM'].item()
                
                # Area of the extracted watershed boundary file in square kilometres
                src_area  = df_gages.loc[df_gages['Monitoring'] == gage_fulnm, 'Area_agg'].item()
                group = run_qaqc(wshd_area=obs_area,
                                 TotDAsqKm=comid_area,
                                 Area_agg =src_area )

            filtered_group_lst = [item for item in group_lst if item != group]
            df_gages.loc[df_gages['Monitoring'] == gage_fulnm, group] = 1
            df_gages.loc[df_gages['Monitoring'] == gage_fulnm, filtered_group_lst] = 0


            gage_filename = "GAGE_ID_" + str(gage_fulnm)
            df_common.to_file(os.path.join(self.output_path.format(Huc_no),"Automatic_Delineation", f"{gage_filename}.shp"))

        df_gages.to_csv(os.path.join(self.Huc_csv_path.format(Huc_no), "check/", file_out), index = False)
        return


def run_qaqc(wshd_area, TotDAsqKm, Area_agg):
    # Description: A validation function to check the accuracy of:
    # 1) COMID assignment ,and 2) the extraction of watershed boundary shapefiles for gauges in Group V 
    
    # Inputs:
    # - wshd_area: ground truth value for the watershed area corresponding to specific gauge in square kilometers
    # - TotDAsqKm: the total drainage area corresponding to a specific COMID according to NHDPlus dataset in square kilometers
    # - Area_agg : the area of the extracted watershed boundary shape file in square kilometers
    
    # Check one: compare wshd_area (if available) to  TotDAsqKm
    if wshd_area != 0.0:
        # check COMID
        delta = np.abs(wshd_area - TotDAsqKm)/ wshd_area * 100
        if delta <=20:
            # check delineation
            # Check two: compare wshd_area (if available) to  Area_agg
            delta = np.abs(wshd_area - Area_agg)/ wshd_area * 100
            if delta <=20:
                out = 'group A' #COMID assignment and Delineation are both valid
            else:
                out = 'group C' #Delineation issues
        else:
            out = 'group B'     #COMID assignment issues
    # Check three: compare TotDAsqKm to  Area_agg
    else:
        delta = np.abs(TotDAsqKm - Area_agg)/ TotDAsqKm * 100
        if delta <= 20:
            out = 'group D'     #Delineation is correct but no ground truth
        else:
            out = 'group C'     #Delineation issues

    return out

def empty_directory(directory):
    folder = directory
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

