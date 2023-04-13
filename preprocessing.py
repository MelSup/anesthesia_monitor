#import packages
import streamlit as st
import pandas as pd
import math
import numpy as np

# data preprocessing
# rename columns
df = pd.read_csv("./data/test_data.csv")
df2=df.rename(columns={'Solar8000/RR_CO2':'rr', 'Solar8000/ST_AVR':'st_avr', 'Orchestra/PPF20_CP':'cp', 
'Orchestra/RFTN20_RATE':'n20_rate', 'Primus/SET_TV_L':'set_tv', 'Primus/FEO2':'feo2', 
'Solar8000/VENT_INSP_TM':'insp_time', 'Primus/TV':'tv', 'EV1000/SVRI':'svri', 'EV1000/SVV':'svv', 
'Solar8000/ART_DBP':'art_dbp', 'Solar8000/VENT_PPLAT':'pplat', 'Primus/SET_PIP':'set_pip', 
'Primus/MAWP_MBAR':'mawp', 'Solar8000/ST_AVF':'st_avf', 'Orchestra/RFTN20_CE':'n20_ce', 'Primus/FEN2O':'fen2o',
'Primus/RR_CO2':'rr_co2', 'EV1000/CVP':'cvp', 'Solar8000/ST_I':'st_i', 'Primus/SET_INSP_TM':'set_insp_time',
'EV1000/SVR':'svr', 'Primus/SET_INSP_PAUSE':'set_insp_pause', 'Solar8000/VENT_RR':'vent_rr', 'Solar8000/ST_III':'st_iii',
'Primus/MV':'mv', 'BIS/BIS':'bis', 'Solar8000/FIO2':'fio2', 'Orchestra/PPF20_CT':'ct', 'BIS/SR':'bis_sr',
'Orchestra/PPF20_CE':'ce', 'BIS/EMG':'bis_emg', 'Solar8000/INCO2':'inco2', 'BIS/TOTPOW':'bis_totpow', 'Primus/COMPLIANCE':'compliance',
'Orchestra/RFTN20_CP':'n20_cp', 'Solar8000/VENT_TV':'vent_tv', 'EV1000/CI':'ci', 'Primus/VENT_LEAK':'vent_leak', 'Primus/MAC':'mac',
'Solar8000/ART_SBP':'art_sbp', 'BIS/SEF':'bis_sef', 'BIS/SQI':'bis_sqi', 'Primus/SET_FRESH_FLOW':'set_fresh_flow', 'Primus/FIO2':'fio2_2',
'Primus/SET_AGE':'age', 'Primus/SET_INTER_PEEP':'set_peep', 'Primus/ETCO2':'etco2', 'Solar8000/VENT_MV':'vent_mv', 'Solar8000/PLETH_HR':'pleth_hr',
'EV1000/SV':'sv', 'Solar8000/HR':'hr', 'Primus/PIP_MBAR':'pip', 'Primus/SET_RR_IPPV':'set_rr_ippv', 'Primus/FLOW_N2O':'flow_n2o', 
'Primus/PAMB_MBAR':'pamb', 'Primus/FLOW_O2':'flow_o2', 'Solar8000/VENT_MAWP':'vent_mawp', 'Orchestra/RFTN20_VOL':'n20_vol', 
'Solar8000/VENT_PIP':'vent_pip', 'Solar8000/ETCO2':'etco2_2', 'Solar8000/NIBP_MBP':'mbp', 'Solar8000/NIBP_DBP':'dbp', 'EV1000/SVI':'svi', 
'Primus/PEEP_MBAR':'peep', 'EV1000/ART_MBP':'art_mbp_2', 'Primus/FLOW_AIR':'flow_air', 'Solar8000/ST_AVL':'st_avl', 'Orchestra/RFTN20_CT':'n20_ct', 
'Solar8000/ART_MBP':'art_mbp', 'Solar8000/ST_II':'st_ii', 'Primus/PPLAT_MBAR':'pplat_2', 'Solar8000/FEO2':'feo2_2', 'Orchestra/PPF20_RATE':'f20_rate',
'EV1000/CO':'co', 'Solar8000/NIBP_SBP':'sbp', 'Solar8000/PLETH_SPO2':'spo2', 'Orchestra/PPF20_VOL':'f20_vol', 'Solar8000/CVP':'cvp_2', 
'Primus/FIN2O':'fin2o', 'Primus/INCO2':'inco2_2'
})
# drop unused columns
df2=df2.drop(columns={'rr','st_avr','cp','n20_rate','set_tv','feo2','insp_time','svri','svv','art_dbp','set_pip','mawp',
'st_avf','n20_ce','fen2o','cvp','st_i','set_insp_time','svr','set_insp_pause','vent_rr','st_iii','mv','fio2',
'ct','bis_sr','ce','bis_emg','inco2','bis_totpow','compliance','n20_cp','vent_tv','ci','vent_leak','art_sbp',
'bis_sef','bis_sqi','set_fresh_flow','fio2_2','age','set_peep','vent_mv','pleth_hr','sv','pip','set_rr_ippv',
'flow_n2o','pamb','flow_o2','vent_mawp','n20_vol','vent_pip','etco2_2','svi','peep','art_mbp_2','flow_air',
'st_avl','n20_ct','art_mbp','st_ii','pplat_2','feo2_2','f20_rate','co','f20_vol','cvp_2','fin2o','inco2_2'})
# duplicate columns
df2['sbp_duplicate'] = df2.loc[:, 'sbp']
df2['dbp_duplicate'] = df2.loc[:, 'dbp']
df2['mbp_duplicate'] = df2.loc[:, 'mbp']
df2['tv_duplicate'] = df2.loc[:, 'tv']
df2['pplat_duplicate'] = df2.loc[:, 'pplat']

# replace missing values with last known value
df2[['etco2','tv','pplat','hr','spo2','rr_co2','sbp','sbp_duplicate','dbp','dbp_duplicate','mbp','mbp_duplicate','tv_duplicate','pplat_duplicate','mac','bis']] = df2[['etco2','tv','pplat','hr','spo2','rr_co2','sbp','sbp_duplicate','dbp','dbp_duplicate','mbp','mbp_duplicate','tv_duplicate','pplat_duplicate','mac','bis']].fillna(method='ffill')
df2['sbp_duplicate'] = df2.sbp_duplicate.loc[df2.sbp_duplicate.shift() != df2['sbp_duplicate']]
df2['dbp_duplicate'] = df2.dbp_duplicate.loc[df2.dbp_duplicate.shift() != df2['dbp_duplicate']]
df2['mbp_duplicate'] = df2.mbp_duplicate.loc[df2.mbp_duplicate.shift() != df2['mbp_duplicate']]
df2['tv_value'] = df2.loc[:, 'tv_duplicate']
df2['pplat_value'] = df2.loc[:, 'pplat_duplicate']
df2[['tv_duplicate','pplat_duplicate','mac']] = df2[['tv_duplicate','pplat_duplicate','mac']].fillna(0)
# change mmHg into kPa for etco2
df2['etco2'] = df2['etco2'].div(7.501).round(1)
df2.insert(12,'max_spo2',100)
df2['relative_tv']= (df2['tv_duplicate']/700)*339
df2['relative_pplat']= (df2['pplat_duplicate']/30)*183
df2['relative_tv'].replace(to_replace = 0, value = 1, inplace=True)
df2['relative_pplat'].replace(to_replace = 0, value = 1, inplace=True)
df2['relative_tv_story'] = df2.loc[:, 'relative_tv']
df2['relative_tv_story'] = df2.relative_tv_story.loc[df2.relative_tv_story.shift(-1) != df2['relative_tv_story']]
df2[['relative_tv_story']] = df2[['relative_tv_story']].fillna(method='ffill')
df2[['relative_tv_story']] = df2[['relative_tv_story']].fillna(1)
df2['relative_pplat_story'] = df2.loc[:, 'relative_pplat']
df2['relative_pplat_story'] = df2.relative_pplat_story.loc[df2.relative_pplat_story.shift(-1) != df2['relative_pplat_story']]
df2[['relative_pplat_story']] = df2[['relative_pplat_story']].fillna(method='ffill')
df2[['relative_pplat_story']] = df2[['relative_pplat_story']].fillna(1)

#adding missing variables
df2.insert(24,'tof',0)
df2.insert(25,'tof_ratio',0)
df2.insert(26,'temp',36)

#reordering dataset
df2 = df2[['time','etco2','tv','relative_tv','relative_tv_story','pplat','relative_pplat','relative_pplat_story','spo2','max_spo2','rr_co2','hr','sbp','sbp_duplicate','mbp','mbp_duplicate','dbp','dbp_duplicate','tof','tof_ratio','mac','bis','temp','tv_duplicate','pplat_duplicate']]
df2=df2.drop(columns=['tv_duplicate','pplat_duplicate'])
st.write(df2)

df2.to_csv('./data/preprocessed_data.csv', index=False)
