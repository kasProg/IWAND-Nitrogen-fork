# IWAND-Nitrogen
![assets](assets/IWAND-Nitrogen.png) 

Water quantity predictions have made tremendous progress, from model development to gaining new knowledge through Large-Sample Hydrology (LSH), going beyond single-case studies and individual rivers. The backbone behind such progress is the availability of a ready-to-use benchmarks such as the CAMELS (Catchment Attributes and Meteorology for Large-sample Studies) dataset. However, large-scale water quality predictions, particularly for nutrients, lag behind due to the scarcity of ready-to-use datasets. We identify four primary limitations in existing water quality datasets: (1) underrepresentation of human-impacted systems, (2) anthropogenic nutrient inputs, (3) incomplete watershed metadata, (4) sparse monitoring coverage. To address these gaps, we have developed the Integrated Watershed Attributes, and Nutrient Data for Nitrogen (IWAND-Nitrogen) dataset, building upon the state-of-the-art CAMELS-Chem dataset for the contiguous United States. The IWAND-Nitrogen dataset includes 574,767 in-situ nitrate (NO3) records from 1,877 different catchments, each with at least 200 measurements from 1980 to 2023. This dataset pairs 88 watershed attributes for both the total upstream area and local corridor, 8 time-series nitrogen input forcings, and 11 climate forcings. IWAND-Nitrogen aims to be a benchmark nutrient dataset for the water quality community, enabling identification of spatiotemporal patterns and hotspots, improving models from catchment to national scales, and advancing understanding of biogeochemical and transport processes in human-impacted systems, and beyond. 
We provide our methodology code, which includes: 
#  1) In-situ data extraction

# (2) Mapping gauges to NHDPlus flowlines

# (3) Watershed attribute extraction

# (4) Watershed boundary delineation from NHDPlus
Our approach to defining watershed boundaries relied on two key strategies: (1)  pairing gauges with watershed data from existing datasets via names/COMIDs, and  (2) developing an automatic watershed extraction algorithm for the rest to effectively handle complexities in manual watershed delineation. We applied the following:
- a) Split the gauges in each HUC into five groups based on name query (Groups I & II), COMID query (Groups III & IV), and the remaining (Group V)

  An example dataset is located in /data/HUC01/csv/
- b) For Group V gauges, run get_UTCOMIDs.R located in /watershedboundary/Rcodes/ to get the upstream COMIDs for each gauge in Group V in all HUCs
- c) run extractshapefiles.py in located in /watershedboundary/pycodes/ to get the shapefiles for each all gauges in each group

# Citation:
Please cite this paper if the code is helpful to you. 
"Insert DOI to our paper"
