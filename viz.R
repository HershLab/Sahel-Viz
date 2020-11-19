library(tmap)
library(sf)
library(tidyverse)

setwd('C:/Users/elmsc/Documents/gis/hersh/Sahel-ID')


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

make_single_map_binary <- function(x,y,name,col,labels,title) {
  country <- aoi %>% filter(COUNTRY == name)
  map <- tm_shape(country) + tm_polygons(col = col, n=2,labels = labels, title = title)
  map <- map + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(x, y))
  
  map
  
  tmap_save(map, filename = paste0("output/", name, "-", col, ".png"))
}

########################################[SIDE BY SIDE MAP]#####################################################

sahel_loc <- 'G:/.shortcut-targets-by-id/1ihZCdFkFKljvEUetC8IiiE7JEDSGKA4J/hersh_lab/sahel/'

aoi <- st_read(paste0(sahel_loc,'combined/shp/sahel.shp'))

aoi <- aoi %>% mutate(DATA_PER_1000 = total/POPULATION*1000,
                      NO_DATA = case_when(total == 0 ~ 0, TRUE ~ 1))

countries <-  unique(aoi$COUNTRY)
countries

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

make_single_map_binary("left", "top", "Benin", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Burkina Faso", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Senegal", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Togo","NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Niger", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Mauritania", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "top", "Mali", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("left", "bottom", "Guinea", "NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Cote dlvoire","NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")
make_single_map_binary("right", "top", "Chad","NO_DATA", c("No Data Available", "Data Available"), "Data Availibility")

########################################[FULL AOI PLOT]#####################################################

map_lights <- tm_shape(aoi) + tm_polygons(col = "NIGHT_LIGH", style = "jenks", title = "Night Lights")
map_lights <- map_lights + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(0,0))

map_data <- tm_shape(aoi) + tm_polygons(col = "DATA_PER_1000", style = "jenks", title = "Data per\n 1000 People")
map_data <- map_data + tm_layout(scale = 1, frame = FALSE) + tm_legend(legend.position = c(0,0))

map <- tmap_arrange(map_lights, map_data)
#map

tmap_save(map, filename = "C:/Users/elmsc/Documents/gis/hersh/Sahel-ID/output/Sahel.png")



