library(nhdplusTools)
library(tidyr)
library(dplyr)

# Read NHDPLUS flowline attributesfor HUC no.{}. Data can be found at https://nhdplus.com/NHDPlus/V2GlobalData.php
network  = read.csv("path to NHDPlus flowline attributes for HUC{}")

# Read gauges in Group V for HUC no.{}. An example dataset is located in the project folder /data/HUC02/csv
df_sites =read.csv("/data/HUC{}/csv/gauges_autodel_{}.csv")

# Extract COMIDs for all gauges
network$COMID = as.integer(network$COMID)

network = select(network, c('COMID', 'Pathlength','LENGTHKM', 'Hydroseq', 'LevelPathI', 'DnHydroseq'))
network = network %>% drop_na()

# Loop through all gauges: 1) get gauge COMID, 2) get gauge_id (name), 3) get upstream COMIDs for this gauge, 4) save them to one csv file
for (i in 1:nrow(df_sites)){
  print(i)
  comid    <- df_sites$COMID[i]
  gauge_id <- df_sites$Monitoring[i]
  df_gauge = data.frame(get_UT(network, comid))
  colnames(df_gauge) = 'COMID'
  write.csv(df_gauge, paste("/data/HUC{}/gauges_UScomids/", gauge_id, "_UTcomids.csv", sep = ""))

}





