

'''
To snap stream gauges to the nearest NHDPlus flowline,
(1) We clipped the CONUS NHDPlus flowline by HUC 2. 

(1) We generated a layer of hub points every 75 meters along the NHDPlus flowlines using the “Points Along Geometry tool” in QGIS, minimizing snapping errors. 
This step was implemented by HUC 2 watershed, due to large data volume

(2) Each stream gauge was then snapped to its nearest hub point, with the assigned COMID and snapping distance recorded using the “QGIS Distance to Nearest Hub” tool. 
This step was implemented by HUC 2 watershed, due to large data volume


'''
import processing
import os
import pandas as pd

p="H:/My Drive/LSTM_NP/Snap_to_NHDPLUS_flowline/"

def clip_nhdplus(in_path, out_path):
    processing.run("gdal:clipvectorbypolygon", { 'INPUT' : in_path, 'OUTPUT' : out_path, 'MASK' : huc })
    
def flowline_hub_points(in_path, out_path):
     processing.run("gdal:clipvectorbypolygon", { { 'DISTANCE' : 75, 'END_OFFSET' : 0, 'INPUT' in_path: , 'OUTPUT' : 'out_path, 'START_OFFSET' : 0 })   
    

def nearest_dis(in_path,out_path,hub_path):
    processing.run("qgis:distancetonearesthubpoints", { 'FIELD' : 'COMID',\
    'HUBS' : hub_path,\
    'INPUT' : pt_path, 'OUTPUT' : out_path, 'UNIT' : 0 })


#define HUC2
l=list(range(1,19))
l= [str(x).zfill(2) for x in l]

#clip nhplus to different HUC2 
for i in l:
    in_path=p+"./NHDPLUS_5070/NHDPLUS_flowline.shp"
    out_path=p+"./NHDPLUS_5070/NHDPLUS_flowline"+i+".shp"
    print(out_path)
    clip_nhdplus(in_path, out_path)

#convert flowline to hub points by HUC2
for i in l:
    in_path=p+"./NHDPLUS_5070/NHDPLUS_flowline"+i+".shp"
    out_path=p+"./NHDPLUS_points/NHDPLUS_pts_75m_"+i+".shp"
    print(out_path)
    flowline_hub_points(in_path, out_path)  

#snap WQP gauge to hub point to get flowline COMID and snapping distance
for i in l:
    in_path="./WQP/WQP_gauges_"+i+".shp"
    hub_path=p+"./NHDPLUS_points/NHDPLUS_pts_75m_"+i+".shp"
    out_path="./SNAP_ID/SNAP_ID_"+i+".shp"
    print(out_path)
    nearest_dis(in_path,out_path,hub_path)   
    





