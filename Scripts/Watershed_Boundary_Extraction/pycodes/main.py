from util import *
from configs.config import *
# Before running this code please check the config.py file located in the project folder /Scripts/Watershed_Boundary_Extraction/configs/)
# to download all the required data

# Initialize the class for extracting watershed boundaries of all gauges in all HUCs
extract_WBD = extract_watershedboundary(SWTrends_path, input_gaugesII_path, catchment_path, Huc_csv_path, UScomids_path,output_path)

# Loop through all the 18 HUCs (An example data for HUC02 is given in the project folder /data/HUC02)
for Huc_no in HUC_no_lst:
    print(Huc_no)
    ###################################################################################################
    for key,value in categories_dict.items():
        filename_cat     = f"gauges_{value}_{Huc_no}.csv"
        filename_cat_out = f"gauges_{value}_{Huc_no}_check.csv"

        if key == 1:
            print("Extracting from GAGES-II by name query, key = 1")
            extract_WBD.extract_gII_gauges(filename_cat,
                                           filename_cat_out,
                                           Huc_no, name = True)

        elif key==2:
            print("Extracting from SWTrends by name query, key = 2")
            extract_WBD.extract_SWTrends_gauges(file_in=filename_cat,
                                                file_out=filename_cat_out,
                                                Huc_no  =Huc_no, name = True)

        elif key == 3:
            print("Extracting from GAGES-II by COMID query, key = 3")
            extract_WBD.extract_gII_gauges(filename_cat,
                                           filename_cat_out,
                                           Huc_no, name = False)
                                      
        elif key==4:
            print("Extracting from SWTrends by COMID query, key = 4")
            extract_WBD.extract_SWTrends_gauges(filename_cat,
                                                filename_cat_out,
                                                Huc_no, name = False)
        elif key == 5:
            print("Automatic watershed extraction algorithm, key = 5")
            extract_WBD.auto_delineate_gauges(filename_cat,
                                              filename_cat_out,
                                              Huc_no)





