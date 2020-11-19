library(tmap)
library(sf)
library(tidyverse)

setwd('C:/Users/elmsc/Documents/gis/hersh/Sahel-Viz')


comparison_map <- function(x,y,name) {
  country <- aoi %>% filter(COUNTRY == name)
  map_lights <- tm_shape(country) + tm_polygons(col = "NIGHT_LIGH", style = "jenks", title = "Night Lights")
  map_lights <- map_lights + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(x, y))
  
  map_data <- tm_shape(country) + tm_polygons(col = "DATA_PER_1000", style = "jenks", title = "Data per 1000 People")
  map_data <- map_data + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(x, y))
  
  map <- tmap_arrange(map_lights, map_data)
  map
  
  tmap_save(map, filename = paste0("output/", name, ".png"))
}

make_single_map <- function(x,y,name,col,title) {
  country <- aoi %>% filter(COUNTRY == name)
  map <- tm_shape(country) + tm_polygons(col = col, style = "jenks", title = title)
  map <- map + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(x, y))
  
  map
  
  tmap_save(map, filename = paste0("output/", name,"i", col, ".png"))
}
tmaptools::palette_explorer()
make_single_map_binary <- function(x,y,name,col,labels,title) {
  country <- aoi %>% filter(COUNTRY == name)
  map <- tm_shape(country) + tm_fill(col = col, style = "cat",palette="Set1", labels = labels, title = title) + tm_borders(col = "black",lwd = 1.5)
  map <- map + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(x, y))
  
  map
  
  tmap_save(map, filename = paste0("output/", name, "-", col, ".png"))
}
make_single_map_binary("left", "top", "Benin", "DATA_AVAILABILITY", c("No Data Available","Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Burkina Faso", "DATA_AVAILABILITY", c("No Data Available","Data Available"), "Data Availibility")

########################################[READ IN DATA]#####################################################

sahel_loc <- 'G:/.shortcut-targets-by-id/1ihZCdFkFKljvEUetC8IiiE7JEDSGKA4J/hersh_lab/sahel/'

aoi <- st_read(paste0(sahel_loc,'combined/shp/sahel.shp'))

aoi <- aoi %>% mutate(DATA_PER_1000 = total/POPULATION*1000,
                      DATA_AVAILABILITY = case_when(total > 0 ~ 1, TRUE ~ 0))

aoi <- aoi %>% mutate(DATA_AVAILABILITY = factor(DATA_AVAILABILITY))

countries <-  unique(aoi$COUNTRY)
countries

########################################[SIDE BY SIDE MAP]#####################################################

comparison_map("left", "top", "Benin")
comparison_map("left", "top", "Burkina Faso")
comparison_map("right", "top", "Senegal")
comparison_map("right", "top", "Togo")
comparison_map("left", "top", "Niger")
comparison_map("left", "top", "Mauritania")
comparison_map("left", "top", "Mali")
comparison_map("left", "bottom", "Guinea")
comparison_map("right", "top", "Cote dlvoire")
comparison_map("right", "top", "Chad")

########################################[SINGLE BINARY]#####################################################

make_single_map_binary("left", "top", "Benin", "DATA_AVAILABILITY", c("Data Available","No Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Burkina Faso", "DATA_AVAILABILITY", c("No Data Available","Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Senegal", "DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Togo","DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Niger", "DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Mauritania", "DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Mali", "DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "bottom", "Guinea", "DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Cote dlvoire","DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Chad","DATA_AVAILABILITY", c("No Data Available", "Data Available"), "Data Availibility")

########################################[FULL AOI PLOT]#####################################################

map_lights <- tm_shape(aoi) + tm_polygons(col = "NIGHT_LIGH", style = "jenks", title = "Night Lights")
map_lights <- map_lights + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(0,0))

map_data <- tm_shape(aoi) + tm_polygons(col = "DATA_PER_1000", style = "jenks", title = "Data per\n 1000 People")
map_data <- map_data + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(0,0))

map <- tmap_arrange(map_lights, map_data)
#map

tmap_save(map, filename = "C:/Users/elmsc/Documents/gis/hersh/Sahel-ID/output/Sahel.png")



