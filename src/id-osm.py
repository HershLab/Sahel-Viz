# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:11:55 2020

@author: elmsc
"""

#%%
import geopandas as gpd
import pandas as pd

#%%
import os
os.chdir('G:/.shortcut-targets-by-id/1ihZCdFkFKljvEUetC8IiiE7JEDSGKA4J/hersh_lab/sahel/')

#%%

sahel = gpd.read_file('combined/shp/sahel.shp')
split = sahel['SSID'].str.split("-",expand=True)
sahel['ID'] = split[1]
del(split)

#%%
# senegal

sen_osm = pd.read_csv('senegal/OSM/senegal_OSM_summary_fix.csv')
sen_osm['name'] = sen_osm['name'].astype(str)
sen = sahel[sahel['COUNTRY'] == 'Senegal']

sen = pd.merge(sen,sen_osm,left_on='ID', right_on='name', how='left')
sen = sen.drop_duplicates(subset=['SSID'], keep='first')

sahel_new = sen

#%%

# togo

togo_osm = pd.read_csv('togo/OSM/Togo_area3_OSM_summary.csv')
togo = sahel[sahel['COUNTRY'] == 'Togo']

togo = pd.merge(togo,togo_osm,left_on='ID', right_on='name', how='left')

togo = togo.drop(columns={'data_per_1k','pop'})

sahel_new = pd.concat([sahel_new, togo],axis=0)


#%%

# niger

niger_osm = pd.read_csv('niger/OSM/Niger_area4_OSM_summary.csv')
niger = sahel[sahel['COUNTRY'] == 'Niger']

niger = pd.merge(niger,niger_osm,left_on='ID', right_on='name', how='left')

niger = niger.drop(columns={'data_per_1k','pop'})

sahel_new = pd.concat([sahel_new, niger],axis=0)
sahel.plot()


#%%

# mauritania
mrt_osm = pd.read_csv('mauritania/OSM/mauritania_area3_OSM_summary.csv')
mrt = sahel[sahel['COUNTRY'] == 'Mauritania']

mrt = pd.merge(mrt,mrt_osm,left_on='ID', right_on='name', how='left')

mrt = mrt.drop(columns={'data_per_1k','pop'})
sahel_new = pd.concat([sahel_new, mrt],axis=0)

#%%

# mali

mali_osm = pd.read_csv('mali/OSM/Mali_admin3_OSM_summary.csv')
mali = sahel[sahel['COUNTRY'] == 'Mali']

mali = pd.merge(mali,mali_osm,left_on='ID', right_on='name', how='left')

mali = mali.drop(columns={'data_per_1k','pop'})
sahel_new = pd.concat([sahel_new, mali],axis=0)

#%%

# guinea

gn_osm = pd.read_csv('guinea/OSM/guinea_area4_OSM_summary.csv')
gn = sahel[sahel['COUNTRY'] == 'Guinea']

gn = pd.merge(gn,gn_osm,left_on='ID', right_on='name', how='left')

gn = gn.drop(columns={'data_per_1k','pop'})
sahel_new = pd.concat([sahel_new, gn],axis=0)

#%%

# cote-dIvoire

civ_osm = pd.read_csv('cote-dIvoire/OSM/civ_area4_OSM_summary.csv')
civ = sahel[sahel['COUNTRY'] == 'Cote dlvoire']

civ = pd.merge(civ,civ_osm,left_on='ID', right_on='name', how='left')

civ = civ.drop(columns={'data_per_1k','pop'})

sahel_new = pd.concat([sahel_new, civ],axis=0)


#%%

# chad

chad_osm = pd.read_csv('chad/OSM/chad_area3_OSM_summary.csv')
chad = sahel[sahel['COUNTRY'] == 'Chad']

chad = pd.merge(chad,chad_osm,left_on='ID', right_on='name', how='left')

chad = chad.drop(columns={'data_per_1k','pop'})

sahel_new = pd.concat([sahel_new, chad],axis=0)

#%%

# burkina-faso

bf_osm = pd.read_csv('burkina-faso/OSM/bf_area4_OSM_summary.csv')
bf = sahel[sahel['COUNTRY'] == 'Burkina Faso']

bf = pd.merge(bf,bf_osm,left_on='ID', right_on='name', how='left')

bf = bf.drop(columns={'data_per_1k','pop'})

sahel_new = pd.concat([sahel_new, bf],axis=0)

#%%

# benin

ben_osm = pd.read_csv('benin/OSM/Benin_area3_OSM_summary.csv')
ben = sahel[sahel['COUNTRY'] == 'Benin']

ben = pd.merge(ben,ben_osm,left_on='ID', right_on='name', how='left')

ben = ben.drop(columns={'data_per_1k','pop'})

sahel_new = pd.concat([sahel_new, ben],axis=0)

#%%

sahel_new.groupby('COUNTRY').agg({"COUNTRY": ["count"]})

sahel_new.to_file('combined/shp/sahel.shp', driver= 'ESRI Shapefile')
