# Load Libraries
library(wqTools)

# 
# downloadWQP(
#   outfile_path = "C:\\Users\\sxc6234\\Downloads",
#   retrieve = c("narrowresult", "sites"),
#   siteType = c("Stream"),
#   statecode = "US:01",
#   zip = FALSE,
#   unzip = FALSE,
#   start_date="01/01/2014",
#   end_date="12/31/2018",
#   characteristicGroup=c("Nutrient"),
# )
# 
# 
# #start_date="01/01/2014"
# #end_date="12/31/2018"
# #  characteristicName=C("Nutrients"),
# 
# 
# downloadWQP(outfile_path="C:\\Users\\sxc6234\\Downloads", start_date="01/01/2018", end_date="12/31/2018", retrieve=c("narrowresult","sites"))
# 
# 
# 
# nr=readWQP(type="narrowresult",
# 	  siteid=c("UTAHDWQ_WQX-4900440","UTAHDWQ_WQX-4900460"),
#  		  characteristicGroup=c("Nutrient"))


#scode=list(01,04,05,06,08,09,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,53,54,55,56)
scode=list(12)
entD =length(scode)
str_lscode<- lapply(scode, function(x) sprintf('%02d', x))


for (j in 1:1) {
  sites=readWQP(type="sites", statecode=paste0("US:", str_lscode[j]), characteristicType=c("Nutrient"),  siteType=c("Stream"),minactivities=30)
  
  #data=readWQP(type="narrowresult", statecode=paste0("US:", str_lscode[j]),   characteristicType=c("Nutrient"),siteType=c("Stream"), minactivities=30)
  
  write.csv(sites, paste0("J:\\My Drive\\LSTM_NP\\WQP\\US",str_lscode[j],"_sites.csv"), row.names=TRUE)
  write.csv(data,  paste0("J:\\My Drive\\LSTM_NP\\WQP\\US",str_lscode[j],"_records.csv"), row.names=TRUE)
  
}

#04 (2) #09 (6) #12(9) #18(22) #19 #20 #21 #23 #31#34

