# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 21:36:41 2025

@author: sxc6234
"""





import processing
import os
import pandas as pd


def nearest_dis(in_path,o_path,hub_path):
    
    processing.run("qgis:distancetonearesthubpoints", { 'FIELD' : 'COMID',\
    'HUBS' : hub_path,\
    'INPUT' : pt_path, 'OUTPUT' : o_path, 'UNIT' : 0 })


p1="J:/My Drive/LSTM_NP/Snap_to_NHDPLUS_flowline/NHDPLUS_points/"

l=list(range(1,19))
l=["{:02}".format(x) for x in l]


for i in l:
    hub_path=p1+"NHDPLUS_pts_75m_"+i+".shp"
    pt_path="H:/My Drive/LSTM_NP/Watershed_Delineation/HUC_"+i+"/csv/"+"gaugeII_huc"+i+"_correctnames.gpkg"
    o_path="H:/My Drive/LSTM_NP/Watershed_Delineation/HUC_"+i+"/csv/"+"gaugeII_huc"+i+"_snapped_correctnames.gpkg"

    nearest_dis(in_path,o_path,hub_path)
