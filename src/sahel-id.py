# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:58:25 2020

@author: elmsc
sahel study id (SSID)

10am
"""
#%%
import geopandas as gpd
import pandas as pd
import fiona

#%%
import os
os.chdir('G:/.shortcut-targets-by-id/1ihZCdFkFKljvEUetC8IiiE7JEDSGKA4J/hersh_lab/sahel/')

#%%
# senegal

gdb_loc = 'senegal/Senegal_geodatabase/SEN.gdb'
layer_list = fiona.listlayers(gdb_loc)
sen = gpd.read_file(gdb_loc, driver='FileGDB', layer='sen_admbnda_adm4_comrurales_gov')

sen['NOMCR'] = sen['NOMCR'].map(lambda x: 'unknown' if x == ' ' else x)
sen = sen.reset_index()
sen['SSID'] = sen['Admi4'].astype(str) + '-' + sen['index'].astype(str)
sen['SSID'] = '0-' + sen['SSID']

sen = sen.rename(columns={'NOMCR':'NAME',
                          'Shape_Area':'AREA'})

sen['COUNTRY'] = 'Senegal'

df = sen[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df.plot()
#%%

# togo

togo = gpd.read_file('togo/boundaries/tgo_admbnda_adm2_1m_gaul_20191003.shp')
togo = togo.reset_index()
togo['SSID'] = togo['ADM2_PCODE'].astype(str) + '-' + togo['index'].astype(str)
togo['SSID'] = '1-' + togo['SSID']

togo = togo.rename(columns={'ADM2_FR':'NAME',
                          'Shape_Area':'AREA'})

togo['COUNTRY'] = 'Togo'

temp = togo[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# niger

niger = gpd.read_file('niger/boundaries/ner_adm03_feb2018/NER_adm03_feb2018.shp')
niger = niger.reset_index()
niger['SSID'] = niger['rowcacode3'].astype(str) +'-' + niger['index'].astype(str)
niger['SSID'] = '2-' + niger['SSID']

niger = niger.rename(columns={'adm_03':'NAME',
                          'Shape_Area':'AREA'})

niger['COUNTRY'] = 'Niger'

temp = niger[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# mauritania

mrt = gpd.read_file('mauritania/mrt_adm_gov_itos_20200801_shp/mrt_admbnda_adm2_gov_20200801.shp')
mrt = mrt.reset_index()
mrt['SSID'] = mrt['ADM2_PCODE'].astype(str) +'-' + mrt['index'].astype(str)
mrt['SSID'] = '3-' + mrt['SSID']

mrt = mrt.rename(columns={'ADM2_EN':'NAME',
                          'Shape_Area':'AREA'})

mrt['COUNTRY'] = 'Mauritania'

temp = mrt[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()



#%%

# mali

mali = gpd.read_file('mali/mli_adm_1m_dnct_2019_shp/mli_admbnda_adm3_1m_dnct_20190802.shp')
mali = mali.reset_index()
mali['SSID'] = mali['admin3Pcod'].astype(str) +'-' + mali['index'].astype(str)
mali['SSID'] = '4-' + mali['SSID']

mali = mali.rename(columns={'admin3Name':'NAME',
                          'Shape_Area':'AREA'})


mali['COUNTRY'] = 'Mali'

temp = mali[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# guinea

gn = gpd.read_file('guinea/boundaries/gin_admbnda_adm3_ocha_itos_03082017/gin_admbnda_adm3_ocha_itos.shp')
gn = gn.reset_index()
gn['SSID'] = gn['admin3Pcod'].astype(str) + '-' +gn['index'].astype(str)
gn['SSID'] = '5-' + gn['SSID']

gn = gn.rename(columns={'admin3Name':'NAME',
                          'Shape_Area':'AREA'})


gn['COUNTRY'] = 'Guinea'

temp = gn[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# cote-dIvoire

civ = gpd.read_file('cote-dIvoire/boundaries/civ_admbnda_adm3_cntig_ocha_itos_20180706/civ_admbnda_adm3_cntig_ocha_itos_20180706.shp')
civ = civ.reset_index()
civ['SSID'] = civ['ADM3_PCODE'].astype(str) +'-' + civ['index'].astype(str)
civ['SSID'] = '6-' + civ['SSID']

civ = civ.rename(columns={'ADM3_FR':'NAME',
                          'Shape_Area':'AREA'})


civ['COUNTRY'] = 'Cote dlvoire'

temp = civ[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# chad

chad = gpd.read_file('chad/boundaries/tcd_admbnda_adm2_ocha_20170615/tcd_admbnda_adm2_ocha_20170615.shp')
chad = chad.reset_index()
chad['SSID'] = chad['admin2Pcod'].astype(str) +'-' + chad['index'].astype(str)
chad['SSID'] = '7-' + chad['SSID']

chad = chad.rename(columns={'admin2RefN':'NAME',
                          'Shape_Area':'AREA'})


chad['COUNTRY'] = 'Chad'

temp = chad[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# burkina-faso

bf = gpd.read_file('burkina-faso/bfa_adm_igb_20200323_shp/bfa_admbnda_adm3_igb_20200323.shp')
bf = bf.reset_index()
bf['SSID'] = bf['ADM3_PCODE'].astype(str) +'-' + bf['index'].astype(str)
bf['SSID'] = '8-' + bf['SSID']

bf = bf.rename(columns={'ADM3_FR':'NAME',
                          'Shape_Area':'AREA'})


bf['COUNTRY'] = 'Burkina Faso'

temp = bf[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

# benin

benin = gpd.read_file('benin/boundaries/Shapefiles/ben_admbnda_adm2_1m_salb_20190816.shp')
benin = benin.reset_index()
benin['SSID'] = benin['ADM2_PCODE'].astype(str) +'-' + benin['index'].astype(str)
benin['SSID'] = '9-' + benin['SSID']

benin = benin.rename(columns={'ADM2_FR':'NAME',
                          'Shape_Area':'AREA'})

benin['COUNTRY'] = 'Benin'

temp = benin[['SSID','COUNTRY', 'NAME', 'AREA', 'geometry']]

df = pd.concat([df,temp], axis=0)
df.plot()

#%%

#DF COMES OUT TO 2795 UNIQUE SUBAREAS

pop = pd.read_csv('combined/csv/sahel_wpop.csv')
pop = pop[['SSID', 'sum']]
pop = pop.rename(columns={'sum':'POPULATION'})
pop = pop.drop_duplicates(subset=['SSID'], keep='first')

df = pd.merge(df, pop, how='inner', on='SSID')

#%%

nl = pd.read_csv('combined/csv/sahel_nightlights.csv')
nl = nl[['SSID', 'sum']]
nl = nl.rename(columns={'sum':'NIGHT_LIGHT'})
nl = nl.drop_duplicates(subset=['SSID'], keep='first')

df = pd.merge(df, nl, how='inner', on='SSID')
#%%

df.to_file('combined/shp/sahel.shp', driver= 'ESRI Shapefile')

df.describe()
