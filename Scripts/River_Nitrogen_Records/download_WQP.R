#This R script pulls stream nutrient data and site metadata from the USGS/EPA Water Quality Portal (WQP) for a #list of U.S. states. For each state, it requests (1) site information and (2) nutrient “narrowresult” records, #limited to stream sites with ≥ 30 activities, and saves them as CSVs in ./data/Records/ using two-digit state codes.
# Load Libraries
library(wqTools)

scode=list(01,04,05,06,08,09,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,53,54,55,56)

entD =length(scode)
str_lscode<- lapply(scode, function(x) sprintf('%02d', x))


for (j in 1:entD) {
  sites=readWQP(type="sites", statecode=paste0("US:", str_lscode[j]), characteristicType=c("Nutrient"),  siteType=c("Stream"),minactivities=30)
  
  data=readWQP(type="narrowresult", statecode=paste0("US:", str_lscode[j]),   characteristicType=c("Nutrient"),siteType=c("Stream"), minactivities=30)
  
  write.csv(sites, paste0("./data/Records/",str_lscode[j],"_sites.csv"), row.names=TRUE)
  write.csv(data,  paste0("./data/Records/",str_lscode[j],"_records.csv"), row.names=TRUE)
  
}


