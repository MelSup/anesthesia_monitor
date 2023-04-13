#import packages
import streamlit as st
import streamlit_nested_layout
import time
import altair as alt
import pandas as pd
import math
import numpy as np
import plotly.graph_objects as go
from PIL import Image,ImageDraw

# page config
st.set_page_config(page_title='anesthesia monitor',
                        layout='wide')

# config plotly indicators
config = {'staticPlot': True}

#load dataset
df = pd.read_csv("./data/scenario4_record.csv")


imgA = Image.open(r'./images/imageA.png').convert('RGBA')
imgC = Image.open(r'./images/imageC.png').convert('RGBA')
img_TOF0 = Image.open(r'./images/TOF0.png').convert('RGBA')
img_TOF1 = Image.open(r'./images/TOF1.png').convert('RGBA')
img_TOF2 = Image.open(r'./images/TOF2.png').convert('RGBA')
img_TOF3 = Image.open(r'./images/TOF3.png').convert('RGBA')
img_TOF4 = Image.open(r'./images/TOF4.png').convert('RGBA')
img_TOFnan = Image.open(r'./images/TOFnan.png').convert('RGBA')
imgD = Image.open(r'./images/imgD.png').convert('RGBA')
imgD_orange = Image.open(r'./images/imgD_orange.png').convert('RGBA')
imgD_red = Image.open(r'./images/imgD_red.png').convert('RGBA')
imgE_ok = Image.open(r'./images/imgE.png').convert('RGBA')
imgE_high = Image.open(r'./images/imgE_high.png').convert('RGBA')
imgE_midhigh = Image.open(r'./images/imgE_midhigh.png').convert('RGBA')
imgE_midlow = Image.open(r'./images/imgE_midlow.png').convert('RGBA')
imgE_low = Image.open(r'./images/imgE_low.png').convert('RGBA')

#variables declaration
position=0
backgroundA = 'grey'
backgroundB = 'grey'
backgroundC = 'grey'
backgroundD = 'grey'
backgroundE = 'grey'
step1_etco2 = 'rgba(105,105,105,255)'
step2_etco2 = 'rgba(128,128,128,255)'
step4_etco2 = 'rgba(128,128,128,255)'
step5_etco2 = 'rgba(105,105,105,255)'
step1_spo2 = 'rgba(105,105,105,255)'
step2_spo2 = 'rgba(128,128,128,255)'
step1_bp = 'rgba(105,105,105,255)'
step2_bp = 'rgba(128,128,128,255)'
step4_bp = 'rgba(128,128,128,255)'
step5_bp = 'rgba(105,105,105,255)'
step1_hr = 'rgba(105,105,105,255)'
step2_hr = 'rgba(128,128,128,255)'
step4_hr = 'rgba(128,128,128,255)'
step5_hr = 'rgba(105,105,105,255)'
step1_rr = 'rgba(105,105,105,255)'
step2_rr = 'rgba(128,128,128,255)'
step4_rr = 'rgba(128,128,128,255)'
step5_rr = 'rgba(105,105,105,255)'
step1_mac = 'rgba(105,105,105,255)'
step2_mac = 'rgba(128,128,128,255)'
step4_mac = 'rgba(128,128,128,255)'
step5_mac = 'rgba(105,105,105,255)'
step1_temp = 'rgba(105,105,105,255)'
step2_temp = 'rgba(128,128,128,255)'
step4_temp = 'rgba(128,128,128,255)'
step5_temp = 'rgba(105,105,105,255)'

BACKGROUND_COLOR = 'white'
COLOR = 'black'

def set_page_container_style(
        max_width: int = 1100, max_width_100_percent: bool = False,
        padding_top: int = 1, padding_right: int = 10, padding_left: int = 1, padding_bottom: int = 10,
        color: str = COLOR, background_color: str = BACKGROUND_COLOR,
    ):
        if max_width_100_percent:
            max_width_str = f'max-width: 100%;'
        else:
            max_width_str = f'max-width: {max_width}px;'
        st.markdown(
            f'''
            <style>
                .reportview-container .sidebar-content {{
                    padding-top: {padding_top}rem;
                }}
                .reportview-container .main .block-container {{
                    {max_width_str}
                    padding-top: {padding_top}rem;
                    padding-right: {padding_right}rem;
                    padding-left: {padding_left}rem;
                    padding-bottom: {padding_bottom}rem;
                }}
                .reportview-container .main {{
                    color: {color};
                    background-color: {background_color};
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

#layout
rowA1,rowA2,rowA3,rowA4,rowA5=st.columns([0.75,1.125,3,1.125,4])
with rowA1:
        caseA = st.empty()
with rowA2:
        test = st.empty()
with rowA3:
        sbs_cols = st. columns ([0.85,0.9,0.5,0.75])
        with sbs_cols[0]:
                st.empty()
        with sbs_cols[1]:       
                imageA = st.empty()
        with sbs_cols[2]:
                gaugeA = st.empty()
        with sbs_cols[3]:
                st.empty()
with rowA4:
        card_etco2 = st.empty()
with rowA5:
        graph_etco2 = st.empty()

rowBC = st.columns([6, 4])

with rowBC[0]:
    
    inner_cols = st.columns([0.75,1.125,3,1.125])
    with inner_cols[0]:
        caseB = st.empty()
        caseC = st.empty()
    with inner_cols[1]:
        card_volume = st.empty()
        card_pressure = st.empty()
        space_bc = st.empty()
        title_heartrate = st.empty()
        gauge_heartrate = st.empty()
    with inner_cols[2]:
        sbs_cols = st. columns ([0.19,2.205,0.5,0.105])
        with sbs_cols[0]:
                st.empty()
        with sbs_cols[1]:
                imageB = st.empty()
                imageC = st.empty()
        with sbs_cols[2]:
                gaugeB = st.empty()
                gaugeC = st.empty()
        with sbs_cols[3]:
                st.empty()

    with inner_cols[3]:
        card_spo2 = st.empty()
        title_resprate = st.empty()
        gauge_resprate = st.empty()
        card_pni = st.empty()

with rowBC[1]:
    inner_graph = st.columns([4])    
    with inner_graph[0]:
        graph_BC = st.empty()

rowD1,rowD2,rowD3,rowD4,rowD5=st.columns([0.75,1.125,3,1.125,4])
with rowD1:
        caseD = st.empty()
with rowD2:
        card_tof = st.empty()
with rowD3:
        sbs_cols = st. columns ([1.25,1,0.75])
        with sbs_cols[0]:
                imageTOF =st.empty()
        with sbs_cols[1]:
                imageD = st.empty()
        with sbs_cols[2]:
                gaugeD = st.empty()
with rowD4:
        card_mac = st.empty()
        card_bis = st.empty()
with rowD5:
        graph_D = st.empty()

rowE1,rowE2,rowE3,rowE4,rowE5=st.columns([0.75,1.125,3,1.125,4])
with rowE1:
        caseE = st.empty()
with rowE2:
        card_temp = st.empty()
with rowE3:
        sbs_cols = st. columns ([0.5,0.7,1.8])
        with sbs_cols[0]:
                gaugeE = st.empty()
        with sbs_cols[1]:
                imageE = st.empty()
        with sbs_cols[2]:
                st.empty()
with rowE4:
        st.empty()
with rowE5:
        graph_E = st.empty()

# variable change
for i in range (len(df)):
  position = position + 1

  time_s=df.iloc[position,0]

  #etco2 for number display
  etco2=df.iloc[position,1]
  if math.isnan(etco2)==True:
          etco2=str('-')
  elif math.isnan(etco2)==False:
          etco2=float(etco2)
  #etco2 for graph
  etco2_value=df.iloc[position,1]
 
  #tv for number display
  tv = df.iloc[position,2]
  if math.isnan(tv)==True:
          tv=str('-')
  elif math.isnan(tv)==False:
          tv=int(tv)
  #tv for height of rectangle
  new_height = int(df.iloc[position,3])
  #old tv for height of trend rectangle
  old_height = int(df.iloc[position,4])
  #tv for if loop (graph)
  tv_value = df.iloc[position,2]

  #pplat for number display
  pplat = df.iloc[position,5]
  if math.isnan(pplat)==True:
          pplat=str('-')
  elif math.isnan(pplat)==False:
          pplat=int(pplat)
  #pplat for width of arrow
  new_width = int(df.iloc[position,6])
  #old pplat for width of trend arrow
  old_width = int(df.iloc[position,7])
  #pplat for if loop (graph)
  pplat_value = df.iloc[position,5]
  
  #spo2 for number display
  spo2 = df.iloc[position,8]
  if math.isnan(spo2)==True:
          spo2=str('-')
  elif math.isnan(spo2)==False:
          spo2=int(spo2)
  #spo2 for if loop (graph)  
  spo2_value = df.iloc[position,8]

   #rr for number display
  rr = df.iloc[position,10]
  if math.isnan(rr)==True:
          rr=str('-')
  elif math.isnan(rr)==False:
          rr=int(rr)
  #rr for if loop (graph)
  rr_value = df.iloc[position,10]

  #hr for number display
  hr = df.iloc[position,11]
  if math.isnan(hr)==True:
          hr=str('-')
  elif math.isnan(hr)==False:
          hr=int(hr)
  #hr for if loop (graph)
  hr_value = df.iloc[position,11]
    

  #sbp/dbp/mbp for number display
  sbp = df.iloc[position,12]
  if math.isnan(sbp)==True:
          sbp=str('-')
  elif math.isnan(sbp)==False:
          sbp=int(sbp)
  dbp = df.iloc[position,16]
  if math.isnan(dbp)==True:
          dbp=str('-')
  elif math.isnan(dbp)==False:
          dbp=int(dbp)
  mbp = df.iloc[position,14]
  if math.isnan(mbp)==True:
          mbp=str('-')
  elif math.isnan(mbp)==False:
          mbp=int(mbp)
  #sbp/dbp/mbp for if loop (graph)
  sbp_value = df.iloc[position,12]
  dbp_value = df.iloc[position,16]
  mbp_value = df.iloc[position,14]
  
  #tof/tof_ratio for number display
  tof = df.iloc[position,18]
  if math.isnan(tof)==True:
          tof=str('-')
  elif math.isnan(tof)==False:
          tof=int(tof)
  tof_ratio = df.iloc[position,19]
  if math.isnan(tof_ratio)==True:
          tof_ratio=str('-')
  elif math.isnan(tof_ratio)==False:
          tof_ratio=int(tof_ratio)

  #tof/tof_ratio for if loop (graph)
  tof_value = df.iloc[position,18]
  tof_ratio_value = df.iloc[position,19]

  #mac/bis for number display
  mac = df.iloc[position,20]
  if math.isnan(mac)==True:
          mac=str('-')
  elif math.isnan(mac)==False:
          mac=float(mac)
  bis = df.iloc[position,21]
  if math.isnan(bis)==True:
          bis=str('-')
  elif math.isnan(bis)==False:
          bis=int(bis)
  
  #mac/bis for if loop (graph)
  mac_value = df.iloc[position,20]
  bis_value = df.iloc[position,21]

  #temp for number display
  temp = df.iloc[position,22]
  if math.isnan(temp)==True:
          temp=str('-')
  elif math.isnan(temp)==False:
          temp=float(temp)
  
  #temp for if loop (graph)
  temp_value = df.iloc[position,22]

  data_to_be_added = df.iloc[0: i + 1, :]
  time.sleep(0.00001)

  with caseA:
        #condition loop to change background color A
        if (    (etco2_value>=3.5) and (etco2_value<=5.5)):
                backgroundA = 'green'
        elif    (((etco2_value<3.5) and (etco2_value>=2.5)) or ((etco2_value>5.5) and (etco2_value<=6.5))):
                backgroundA = 'orange'
        elif    ((etco2_value<2.5) or (etco2_value>6.5)):
                backgroundA = 'red'
        else:
                backgroundA = 'grey'

        st.markdown('<h1 style="text-align: center; line-height:2.4; background-color: {}">A</h1>'.format(backgroundA), unsafe_allow_html=True)

  with imageA:
        # image A
        st.image(imgA,use_column_width=True)

  with gaugeA:
         
          #condition loop to change background color in gauge
          if (etco2_value<2.5):
                step1_etco2='rgba(255,0,0,0.5)'
                step2_etco2 = 'rgba(128,128,128,255)'
                step4_etco2 = 'rgba(128,128,128,255)'
                step5_etco2 = 'rgba(105,105,105,255)'
          elif ((etco2_value<3.5) and (etco2_value>=2.5)):
                step2_etco2='rgba(255,128,0,0.5)'
                step1_etco2 = 'rgba(105,105,105,255)'
                step4_etco2 = 'rgba(128,128,128,255)'
                step5_etco2 = 'rgba(105,105,105,255)'
          elif ((etco2_value>5.5) and (etco2_value<=6.5)):
                step4_etco2='rgba(255,128,0,0.5)'
                step1_etco2 = 'rgba(105,105,105,255)'
                step2_etco2 = 'rgba(128,128,128,255)'
                step5_etco2 = 'rgba(105,105,105,255)'
          elif    (etco2_value>6.5):
                step5_etco2 = 'rgba(255,0,0,0.5)'
                step1_etco2 = 'rgba(105,105,105,255)'
                step2_etco2 = 'rgba(128,128,128,255)'
                step4_etco2 = 'rgba(128,128,128,255)'
          else:
                step1_etco2 = 'rgba(105,105,105,255)'
                step2_etco2 = 'rgba(128,128,128,255)'
                step4_etco2 = 'rgba(128,128,128,255)'
                step5_etco2 = 'rgba(105,105,105,255)'

          gaugeAData = pd.DataFrame({
                  'min':[0],
                  'level1':[2.5],
                  'level2':[3.5],
                  'level3':[5.5],
                  'level4':[6.5],
                  'max':[15],
                  'value':etco2_value
                  })

          max = alt.Chart(gaugeAData).mark_bar(color=step5_etco2).encode(alt.Y("level4:Q", scale=alt.Scale(domain=(0,15)),title=None, axis=alt.Axis(orient='right')),y2="max:Q")
          level4 = alt.Chart(gaugeAData).mark_bar(color=step4_etco2).encode(alt.Y("level3:Q", scale=alt.Scale(domain=(0,15)),title=None, axis=alt.Axis(orient='right')),y2="level4:Q")
          level3 = alt.Chart(gaugeAData).mark_bar(color='#A9A9A9').encode(alt.Y("level2:Q", scale=alt.Scale(domain=(0,15)),title=None, axis=alt.Axis(orient='right')),y2="level3:Q")
          level2 = alt.Chart(gaugeAData).mark_bar(color=step2_etco2).encode(alt.Y("level1:Q", scale=alt.Scale(domain=(0,15)),title=None, axis=alt.Axis(orient='right')),y2="level2:Q")
          level1 = alt.Chart(gaugeAData).mark_bar(color=step1_etco2).encode(alt.Y("min:Q", scale=alt.Scale(domain=(0,15)),title=None, axis=alt.Axis(orient='right')),y2="level1:Q")
          valueLine=alt.Chart(gaugeAData).mark_bar(size=8,color='white',opacity=1).encode( y=alt.Y("min:Q",scale=alt.Scale(domain=(0,15)),title=None , axis=alt.Axis(orient='right')),y2="value:Q")

          fig_gaugeA = alt.layer(max,level4,level3,level2,level1,valueLine,width=40, height=115, padding={"left": 0, "right": 0, "bottom": 0, "top": 0})
          
          gaugeA.altair_chart(fig_gaugeA)

  with card_etco2:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;">EtCO2<a style="float: right; font-size:14px; vertical-align: bottom;">kPa</a></div></ br><div style="text-align: center;font-size:24px">{}</div>'.format(etco2), unsafe_allow_html=True)
        
  with graph_etco2:
          base = alt.Chart(data_to_be_added, padding={"left": 0, "top": 0, "right": 0, "bottom": 0}).mark_area(opacity=0.5).encode(
                  x=alt.X('time', axis=alt.Axis(title=None),scale=alt.Scale(padding=0)),
                  y=alt.Y('etco2', axis=alt.Axis(title=None),scale=alt.Scale(domain=[0, 15],padding=0)),
                  color=alt.value("white")
                  ).properties(height=115)
          graph_etco2.altair_chart(base,use_container_width=True)

  with caseB:
        #condition loop to change background color B
        if math.isnan(spo2_value) and math.isnan(rr_value) and math.isnan(tv_value) and math.isnan(pplat_value):
                backgroundB = 'grey'
        elif (spo2_value<88) or (rr_value<6) or (rr_value>25) or (tv_value>850) or (tv_value<350) or (pplat_value>30) or (pplat_value<3):
                backgroundB = 'red'
        elif ((spo2_value<94) and (spo2_value>=88)) or ((rr_value<10) and (rr_value>=6)) or ((rr_value>20) and (rr_value<=25)) or ((tv_value>700) and (tv_value<=850)) or ((tv_value<400) and (tv_value>=350)) or ((pplat_value>25) and (pplat_value<=30)) or ((pplat_value<5) and (pplat_value>=3)):
                backgroundB = 'orange'
        elif (math.isnan(spo2_value) or spo2_value>=94) and (math.isnan(rr_value) or ((rr_value>=10) and (rr_value<=20))) and (math.isnan(tv_value) or ((tv_value>=400) and (tv_value<=700))) and (math.isnan(pplat_value) or ((pplat_value>=5) and (pplat_value<=25))):
                backgroundB = 'green'
        else:
                backgroundB = 'grey'
        
        st.markdown('<h1 style="text-align: center; line-height:3.5; background-color: {}">B</h1>'.format(backgroundB), unsafe_allow_html=True)

  with caseC:
        #condition loop to change background color C
        if math.isnan(hr_value) and math.isnan(sbp_value) and math.isnan(dbp_value) and math.isnan(mbp_value):
                backgroundC = 'grey'
        elif (hr_value>120) or (hr_value<45) or (sbp_value<80) or (sbp_value>150) or (dbp_value<40) or (dbp_value>100) or (mbp_value<50) or (mbp_value>120):
                backgroundC = 'red'
        elif ((hr_value>100) and (hr_value<=120)) or ((hr_value<60) and (hr_value>=45)) or ((sbp_value<90) and (sbp_value>=80)) or ((sbp_value>135) and (sbp_value<=150)) or ((dbp_value<60) and (dbp_value>=40)) or ((dbp_value>80) and (dbp_value<=100)) or ((mbp_value<60) and (mbp_value>=50)) or ((mbp_value>100) and (mbp_value<=120)):
                backgroundC = 'orange'
        elif (math.isnan(hr_value) or ((hr_value>=60) and (hr_value<=100))) and (math.isnan(sbp_value) or ((sbp_value>=90) and (sbp_value<=135))) and (math.isnan(dbp_value) or ((dbp_value>=60) and (dbp_value<=80))) and (math.isnan(mbp_value) or ((mbp_value>=60) and (mbp_value<=100))):
                backgroundC = 'green'
        else:
                backgroundC = 'grey'  
        st.markdown('<h1 style="text-align: center; line-height:3.15; background-color: {}">C</h1>'.format(backgroundC), unsafe_allow_html=True)

  with imageB:
        #condition loops to ensure dimensions inside image B
        if new_height>444:
               new_height=444
        elif new_height<1:
                new_height=1
        else: 
                new_height=new_height

        if old_height>444:
               old_height=444
        elif old_height<1:
               old_height=1
        else: 
                old_height=old_height
        
        if new_width>400:
               new_width=400    
        elif new_width<1:
                new_width=1
        else: 
                new_width=new_width

        if old_width>400:
               old_width=400
        elif old_width<1:
               old_width=1
        else: 
                old_width=old_width

        # background image B
        imgB1 = Image.open(r'./images/imageB.png').convert('RGBA')
        imgB2 = Image.open(r'./images/arrow.png').convert('RGBA')
        imgB3 = Image.open(r'./images/arrow_border.png').convert('RGBA')
        new = Image.new('RGBA',imgB1.size,(255,255,255,0))
        rectangle_fill = [(206, 445-new_height), (402, 445)]
        rectangle_old = [(206, 445-old_height), (402, 445)]
        rectangle_box = [(204, 104), (404, 447)]
        arrow_box = [(420, 272), (612, 400)]  #changé taille box de 608 à 612
        draw=ImageDraw.Draw(new,'RGBA')
        draw.rectangle(rectangle_fill,fill=(0,0,255,128))
        draw.rectangle(rectangle_old,outline=(157,223,255,255),width=2)
        draw.rectangle(rectangle_box,outline="#A9A9A9",width=3)
        draw.rectangle(arrow_box,outline="#A9A9A9",width=3)
        width_arrow,height_arrow = imgB2.size
        imgB2 = imgB2.resize((new_width,height_arrow), Image.Resampling.NEAREST)
        imgB3 = imgB3.resize((old_width,height_arrow), Image.Resampling.NEAREST)
        imgB1.paste(imgB2,(422,275),mask=imgB2)
        imgB1.paste(imgB3,(422,275),mask=imgB3)
        out= Image.alpha_composite(imgB1,new)
        st.image(out,use_column_width=True)

  with imageC:
        # background image C
        st.image(imgC,use_column_width=True)     

  with gaugeB:
        #condition loop to change background color in gauge
        if (spo2_value<88):
                step1_spo2='rgba(255,0,0,0.5)'
                step2_spo2 = 'rgba(128,128,128,255)'
        elif ((spo2_value<94) and (spo2_value>=88)):
                step2_spo2='rgba(255,128,0,0.5)'
                step1_spo2 = 'rgba(105,105,105,255)'
        else:
                step1_spo2 = 'rgba(105,105,105,255)'
                step2_spo2 = 'rgba(128,128,128,255)'

        gaugeBData = pd.DataFrame({
                  'min':[0],
                  'level1':[88],
                  'level2':[94],
                  'max':[100],
                  'value':spo2_value
                  })

        max = alt.Chart(gaugeBData).mark_bar(color='#A9A9A9').encode(alt.Y("level2:Q", scale=alt.Scale(domain=(0,100)),title=None, axis=alt.Axis(orient='right')),y2="max:Q")
        level2 = alt.Chart(gaugeBData).mark_bar(color=step2_spo2).encode(alt.Y("level1:Q", scale=alt.Scale(domain=(0,100)),title=None, axis=alt.Axis(orient='right')),y2="level2:Q")
        level1 = alt.Chart(gaugeBData).mark_bar(color=step1_spo2).encode(alt.Y("min:Q", scale=alt.Scale(domain=(0,100)),title=None, axis=alt.Axis(orient='right')),y2="level1:Q")
        valueLine=alt.Chart(gaugeBData).mark_bar(size=8,color='yellow',opacity=1).encode( y=alt.Y("min:Q",scale=alt.Scale(domain=(0,100)),title=None , axis=alt.Axis(orient='right')),y2="value:Q")

        fig_gaugeB = alt.layer(max,level2,level1,valueLine, width=45, height=135)
          
        gaugeB.altair_chart(fig_gaugeB)       

  with gaugeC:
        #condition loop to change background color in gauge
        if (mbp_value<50):
                step1_bp= 'rgba(255,0,0,0.5)'
                step2_bp = 'rgba(128,128,128,255)'
                step4_bp = 'rgba(128,128,128,255)'
                step5_bp = 'rgba(105,105,105,255)'
        elif ((mbp_value<60) and (mbp_value>=50)):
                step2_bp='rgba(255,128,0,0.5)'
                step1_bp = 'rgba(105,105,105,255)'
                step4_bp = 'rgba(128,128,128,255)'
                step5_bp = 'rgba(105,105,105,255)'
        elif ((mbp_value>100) and (mbp_value<=120)):
                step4_bp ='rgba(255,128,0,0.5)'
                step1_bp = 'rgba(105,105,105,255)'
                step2_bp = 'rgba(128,128,128,255)'
                step5_bp = 'rgba(105,105,105,255)'
        elif  (mbp_value>120):
                step5_bp = 'rgba(255,0,0,0.5)'
                step1_bp = 'rgba(105,105,105,255)'
                step2_bp = 'rgba(128,128,128,255)'
                step4_bp = 'rgba(128,128,128,255)'
        else:
                step1_bp = 'rgba(105,105,105,255)'
                step2_bp = 'rgba(128,128,128,255)'
                step4_bp = 'rgba(128,128,128,255)'
                step5_bp = 'rgba(105,105,105,255)'                      

        gaugeCData = pd.DataFrame({
                  'min':[0],
                  'level1':[50],
                  'level2':[60],
                  'level3':[100],
                  'level4':[120],
                  'max':[250],
                  'value1':sbp_value,
                  'value2':dbp_value,
                  'value3':mbp_value
                  })

        max = alt.Chart(gaugeCData).mark_bar(color=step5_bp).encode(alt.Y("level4:Q", scale=alt.Scale(domain=(0,250)),title=None, axis=alt.Axis(orient='right')),y2="max:Q")
        level4 = alt.Chart(gaugeCData).mark_bar(color=step4_bp).encode(alt.Y("level3:Q", scale=alt.Scale(domain=(0,250)),title=None, axis=alt.Axis(orient='right')),y2="level4:Q")
        level3 = alt.Chart(gaugeCData).mark_bar(color='#A9A9A9').encode(alt.Y("level2:Q", scale=alt.Scale(domain=(0,250)),title=None, axis=alt.Axis(orient='right')),y2="level3:Q")
        level2 = alt.Chart(gaugeCData).mark_bar(color=step2_bp).encode(alt.Y("level1:Q", scale=alt.Scale(domain=(0,250)),title=None, axis=alt.Axis(orient='right')),y2="level2:Q")
        level1 = alt.Chart(gaugeCData).mark_bar(color=step1_bp).encode(alt.Y("min:Q", scale=alt.Scale(domain=(0,250)),title=None, axis=alt.Axis(orient='right')),y2="level1:Q")
        point = alt.Chart(gaugeCData).mark_point(filled=True,size=90,color='fuchsia',opacity=1).encode( y=alt.Y('value3',scale=alt.Scale(domain=(0,250)),title=None , axis=alt.Axis(orient='right')))
        #bar = alt.Chart(gaugeCData).mark_errorbar(color='fuchsia',ticks=True,opacity=1).encode( y=alt.Y('value1',scale=alt.Scale(domain=(0,250)),title=None , axis=alt.Axis(orient='right')),y2='value2')
        
        fig_gaugeC = alt.layer(max,level4,level3,level2,level1,point,width=45, height=150, padding={"left": 0, "top": 40, "right": 0, "bottom": 0})
          
        gaugeC.altair_chart(fig_gaugeC)

  with card_volume:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color: royalblue">TV<a style="float: right; font-size:14px; vertical-align: bottom;">ml</a></div></ br><div style="text-align: center;font-size:24px;color: royalblue">{}</div>'.format(tv), unsafe_allow_html=True)

  with card_pressure:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:orange">Pplat<a style="float: right; font-size:14px; vertical-align: bottom;">cmH2O</a></div></ br><div style="text-align: center;font-size:24px;color:orange">{}</div>'.format(pplat), unsafe_allow_html=True)

  with space_bc:
        st.markdown('<h1 style="font-size:50px; height:80px;"></h1>', unsafe_allow_html=True)

  with title_heartrate:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:#AAFF00">HR<a style="float: right; font-size:14px; vertical-align: bottom;">/min</a></div>', unsafe_allow_html=True)  
  
  with gauge_heartrate:
        #condition loop to change background color in gauge
        if (hr_value<45):
                step1_hr='rgba(255,0,0,0.5)'
                step2_hr = 'rgba(128,128,128,255)'
                step4_hr = 'rgba(128,128,128,255)'
                step5_hr = 'rgba(105,105,105,255)'
        elif ((hr_value<60) and (hr_value>=45)):
                step2_hr='rgba(255,128,0,0.5)'
                step1_hr = 'rgba(105,105,105,255)'
                step4_hr = 'rgba(128,128,128,255)'
                step5_hr = 'rgba(105,105,105,255)'
        elif ((hr_value>100) and (hr_value<=120)):
                step4_hr='rgba(255,128,0,0.5)'
                step1_hr = 'rgba(105,105,105,255)'
                step2_hr = 'rgba(128,128,128,255)'
                step5_hr = 'rgba(105,105,105,255)'
        elif  (hr_value>120):
                step5_hr = 'rgba(255,0,0,0.5)'
                step1_hr = 'rgba(105,105,105,255)'
                step2_hr = 'rgba(128,128,128,255)'
                step4_hr = 'rgba(128,128,128,255)'
        else:
                step1_hr = 'rgba(105,105,105,255)'
                step2_hr = 'rgba(128,128,128,255)'
                step4_hr = 'rgba(128,128,128,255)'
                step5_hr = 'rgba(105,105,105,255)'
                

        fig_gauge_heartrate = go.Figure(data=go.Indicator(
                mode = "gauge+number",
                value = hr_value,
                number_font_size = 24,
                number_font_color='#AAFF00',
                gauge_axis_tickfont_size=12,
                legendgrouptitle_font_color='white',
                domain = {'x': [0, 1], 'y': [0, 1]},
                gauge = {
                        'axis': {'range': [None, 220], 'tickwidth': 1, 'tickcolor': "white"},
                        'bar': {'color': "#AAFF00"},
                        'bgcolor': "black",
                        'borderwidth': 2,
                        'bordercolor': "black",
                        'steps': [
                        {'range': [0, 45], 'color': step1_hr},
                        {'range': [45, 60], 'color': step2_hr},
                        {'range': [60, 100], 'color': '#A9A9A9'},
                        {'range': [100, 120], 'color': step4_hr},
                        {'range': [120, 220], 'color': step5_hr}],
                        })
                )

        fig_gauge_heartrate.update_layout(yaxis=dict(automargin=False), height=100, margin=dict(t=0,l=1.5,b=0,r=1.5,pad=0,autoexpand=False), autosize = False)
        st.plotly_chart(fig_gauge_heartrate, config=config, use_container_width=True)

  with card_spo2:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:yellow">SpO2<a style="float: right; font-size:14px; vertical-align: bottom;">%</a></div></ br><div style="text-align: center;font-size:24px;color:yellow">{}</div>'.format(spo2), unsafe_allow_html=True)

  with title_resprate:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:lightblue">RR<a style="float: right; font-size:14px; vertical-align: bottom;">/min</a></div>', unsafe_allow_html=True)

  with gauge_resprate:
        #condition loop to change background color in gauge
        if (rr_value<6):
                step1_rr='rgba(255,0,0,0.5)'
                step2_rr = 'rgba(128,128,128,255)'
                step4_rr = 'rgba(128,128,128,255)'
                step5_rr = 'rgba(105,105,105,255)'
        elif ((rr_value<10) and (rr_value>=6)):
                step2_rr='rgba(255,128,0,0.5)'
                step1_rr = 'rgba(105,105,105,255)'
                step4_rr = 'rgba(128,128,128,255)'
                step5_rr = 'rgba(105,105,105,255)'
        elif ((rr_value>20) and (rr_value<=25)):
                step4_rr='rgba(255,128,0,0.5)'
                step1_rr = 'rgba(105,105,105,255)'
                step2_rr = 'rgba(128,128,128,255)'
                step5_rr = 'rgba(105,105,105,255)'
        elif  (rr_value>25):
                step5_rr = 'rgba(255,0,0,0.5)'
                step1_rr = 'rgba(105,105,105,255)'
                step2_rr = 'rgba(128,128,128,255)'
                step4_rr = 'rgba(128,128,128,255)'
        else:
                step1_rr = 'rgba(105,105,105,255)'
                step2_rr = 'rgba(128,128,128,255)'
                step4_rr = 'rgba(128,128,128,255)'
                step5_rr = 'rgba(105,105,105,255)'

        fig_gauge_resprate = go.Figure(data=go.Indicator(
                mode = "gauge+number",
                value = rr_value,
                number_font_size = 24,
                number_font_color='lightblue',
                gauge_axis_tickfont_size=12,
                legendgrouptitle_font_color='white',
                domain = {'x': [0, 1], 'y': [0, 1]},
                gauge = {
                        'axis': {'range': [None, 60], 'tickwidth': 1, 'tickcolor': "white"},
                        'bar': {'color': "lightblue"},
                        'bgcolor': "black",
                        'borderwidth': 2,
                        'bordercolor': "black",
                        'steps': [
                        {'range': [0, 6], 'color': step1_rr},
                        {'range': [6, 10], 'color': step2_rr},
                        {'range': [10, 20], 'color': '#A9A9A9'},
                        {'range': [20, 25], 'color': step4_rr},
                        {'range': [25, 60], 'color': step5_rr}],
                        })
                )

        fig_gauge_resprate.update_layout(yaxis=dict(automargin=False), height=100, margin=dict(t=0,l=1.5,b=0,r=1.5,pad=0,autoexpand=False), autosize = False)
        st.plotly_chart(fig_gauge_resprate, config=config, use_container_width=True)

  with card_pni:
        st.markdown('<div style="text-align: left; font-size: 18px; vertical-align: middle;color: fuchsia">NIBP<a style="float: right;font-size:14px; vertical-align: bottom;">mmHg</a></div></ br><div style="text-align: center; font-size: 24px; color: fuchsia">{}/{} ({})</div>'.format(sbp,dbp,mbp), unsafe_allow_html=True)

  with graph_BC:
          resprate = alt.Chart(data_to_be_added).mark_line(opacity=1).encode(
                  x=alt.X('time'),
                  y=alt.Y('rr_co2', axis=alt.Axis(title=None, orient='left'),scale=alt.Scale(domain=[0, 100],padding=0)),
                  color=alt.value("lightblue")
                  )
          heartrate = alt.Chart(data_to_be_added).mark_line(opacity=1).encode(
                  x=alt.X('time'),
                  y=alt.Y('hr', axis=alt.Axis(title=None, orient='right'),scale=alt.Scale(domain=[0, 250],padding=0)),
                  color=alt.value("#AAFF00")
                  )
          sat = alt.Chart(data_to_be_added).mark_area(opacity=0.5).encode(
                  x=alt.X('time'),
                  y=alt.Y('spo2',axis=alt.Axis(title=None, orient='left'),scale=alt.Scale(domain=[0, 100],padding=0)),
                  y2='max_spo2',
                  color=alt.value("yellow")
                  )
        # generate the points
          points = alt.Chart(data_to_be_added).mark_point(
                  filled=True,
                  size=50,
                  color='fuchsia'
                  ).encode(
                  x=alt.X('time', axis=alt.Axis(title=None)),
                  y=alt.Y('mbp_duplicate',axis=alt.Axis(title=None, orient='right'),scale=alt.Scale(domain=[0, 250],padding=0)),
          )

        # generate the error bars
          errorbars = alt.Chart(data_to_be_added).mark_errorbar(
            color='fuchsia',
            ticks=True 
                ).encode(
                x=alt.X('time'),
                y=alt.Y('sbp_duplicate',axis=alt.Axis(title=None, orient='right'),scale=alt.Scale(domain=[0, 250],padding=0)),
                y2='dbp_duplicate'
          )
          
          fig_graphBC = alt.layer(points,errorbars,sat,resprate,heartrate).resolve_scale(y='independent').properties(height=335, width=525)
       
          graph_BC.altair_chart(fig_graphBC, use_container_width=False)

  with caseD:
        #condition loop to change background color D
        if (    (bis_value>=40) and (bis_value<=60)):
                backgroundD = 'green'
        elif    (((bis_value<40) and (bis_value>=20)) or ((bis_value>60) and (bis_value<=70))):
                backgroundD = 'orange'
        elif    ((bis_value<20) or (bis_value>70)):
                backgroundD = 'red'
        else:
                backgroundD = 'grey'

        st.markdown('<h1 style="text-align: center; line-height:2.8; background-color: {}">D</h1>'.format(backgroundD), unsafe_allow_html=True)
  
  with card_tof:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:#AFE1AF">TOF<a style="float: right; font-size:14px; vertical-align: bottom;">%</a></div></ br><div style="text-align: center;font-size:24px;color:#AFE1AF">{}</div>'.format(tof_ratio), unsafe_allow_html=True) 

  with imageTOF:
        img_TOF = img_TOFnan
        
        #condition loop to change image TOF
        if (tof_value==0):
                img_TOF = img_TOF0
        elif (tof_value==1):
                img_TOF = img_TOF1
        elif (tof_value==2):
                img_TOF = img_TOF2
        elif (tof_value==3):
                img_TOF = img_TOF3
        elif (tof_value==4):
                img_TOF = img_TOF4
        else:
                img_TOF = img_TOFnan
        st.image(img_TOF,use_column_width=True)

  with imageD:
        #condition loop to change image depending on bis value
        if (((bis_value<40) and (bis_value>=20)) or ((bis_value>60) and (bis_value<=70))):
                imgD_on = imgD_orange
        elif ((bis_value<20) or (bis_value>70)):
                imgD_on = imgD_red
        else:
                imgD_on = imgD
        # image D
        st.image(imgD_on,use_column_width=True)

  with gaugeD:
        #condition loop to change background color in gauge
        if (mac_value<0.7):
                step1_mac='rgba(255,0,0,0.5)'
                step2_mac = 'rgba(128,128,128,255)'
                step4_mac = 'rgba(128,128,128,255)'
                step5_mac = 'rgba(105,105,105,255)'
        elif ((mac_value<0.8) and (mac_value>=0.7)):
                step2_mac ='rgba(255,128,0,0.5)'
                step1_mac = 'rgba(105,105,105,255)'
                step4_mac = 'rgba(128,128,128,255)'
                step5_mac = 'rgba(105,105,105,255)'
        elif ((mac_value>1.2) and (mac_value<=1.3)):
                step4_mac ='rgba(255,128,0,0.5)'
                step1_mac = 'rgba(105,105,105,255)'
                step2_mac = 'rgba(128,128,128,255)'
                step5_mac = 'rgba(105,105,105,255)'
        elif  (mac_value>1.3):
                step5_mac = 'rgba(255,0,0,0.5)'
                step1_mac = 'rgba(105,105,105,255)'
                step2_mac = 'rgba(128,128,128,255)'
                step4_mac = 'rgba(128,128,128,255)'
        else:
                step1_mac = 'rgba(105,105,105,255)'
                step2_mac = 'rgba(128,128,128,255)'
                step4_mac = 'rgba(128,128,128,255)'
                step5_mac = 'rgba(105,105,105,255)'

        gaugeDData = pd.DataFrame({
                  'min':[0],
                  'level1':[0.7],
                  'level2':[0.8],
                  'level3':[1.2],
                  'level4':[1.3],
                  'max':[2],
                  'value':mac_value
                  })

        max = alt.Chart(gaugeDData).mark_bar(color=step5_mac).encode(alt.Y("level4:Q", scale=alt.Scale(domain=(0,2)),title=None, axis=alt.Axis(orient='right')),y2="max:Q")
        level4 = alt.Chart(gaugeDData).mark_bar(color=step4_mac).encode(alt.Y("level3:Q", scale=alt.Scale(domain=(0,2)),title=None, axis=alt.Axis(orient='right')),y2="level4:Q")
        level3 = alt.Chart(gaugeDData).mark_bar(color='#A9A9A9').encode(alt.Y("level2:Q", scale=alt.Scale(domain=(0,2)),title=None, axis=alt.Axis(orient='right')),y2="level3:Q")
        level2 = alt.Chart(gaugeDData).mark_bar(color=step2_mac).encode(alt.Y("level1:Q", scale=alt.Scale(domain=(0,2)),title=None, axis=alt.Axis(orient='right')),y2="level2:Q")
        level1 = alt.Chart(gaugeDData).mark_bar(color=step1_mac).encode(alt.Y("min:Q", scale=alt.Scale(domain=(0,2)),title=None, axis=alt.Axis(orient='right')),y2="level1:Q")
        valueLine=alt.Chart(gaugeDData).mark_bar(size=8,color='#DDA0DD',opacity=1).encode( y=alt.Y("min:Q",scale=alt.Scale(domain=(0,2)),title=None , axis=alt.Axis(orient='right')),y2="value:Q")

        fig_gaugeD = alt.layer(max,level4,level3,level2,level1,valueLine, width=43, height=135)
          
        gaugeD.altair_chart(fig_gaugeD)

  with card_mac:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:#DDA0DD">MAC<a style="float: right; font-size:14px; vertical-align: bottom;"></a></div></ br><div style="text-align: center;font-size:24px;color:#DDA0DD">{}</div>'.format(mac), unsafe_allow_html=True) 
  
  with card_bis:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:#FA8072">BIS<a style="float: right; font-size:14px; vertical-align: bottom;"></a></div></ br><div style="text-align: center;font-size:24px;color:#FA8072">{}</div>'.format(bis), unsafe_allow_html=True)

  with graph_D:
        bis_percent = alt.Chart(data_to_be_added).mark_line(opacity=1).encode(
                x=alt.X('time'),
                y=alt.Y('bis', axis=alt.Axis(title=None),scale=alt.Scale(domain=[0, 100],padding=0)),
                color=alt.value("#FA8072")
        )

        mac_percent = alt.Chart(data_to_be_added).mark_line(opacity=1).encode(
                x=alt.X('time', axis=alt.Axis(title=None)),
                y=alt.Y('mac', axis=alt.Axis(title=None, orient='right'),scale=alt.Scale(domain=[0, 2],padding=0)),
                color=alt.value("#DDA0DD")
        )

        fig_graphD = alt.layer(bis_percent,mac_percent).resolve_scale(y='independent').properties(height=130,width=517)
        
        graph_D.altair_chart(fig_graphD, use_container_width=False)

  with caseE:
        #condition loop to change background color E
        if (    (temp_value>=35.5) and (temp_value<=37.5)):
                backgroundE = 'green'
        elif    (((temp_value<35.5) and (temp_value>=34.5)) or ((temp_value>37.5) and (temp_value<=38.3))):
                backgroundE = 'orange'
        elif    ((temp_value<34.5) or (temp_value>38.3)):
                backgroundE = 'red'
        else:
                backgroundE = 'grey'

        st.markdown('<h1 style="text-align: center; line-height:1.9; background-color: {}">E</h1>'.format(backgroundE), unsafe_allow_html=True)

  with card_temp:
        st.markdown('<div style="text-align: left; font-size:18px;vertical-align: middle;color:#7393B3">T<a style="float: right; font-size:14px; vertical-align: bottom;">°C</a></div></ br><div style="text-align: center;font-size:24px;color:#7393B3">{}</div>'.format(temp), unsafe_allow_html=True)

  with gaugeE:
        #condition loop to change background color in gauge
        if (temp_value<35):
                step1_temp='rgba(255,0,0,0.5)'
                step2_temp = 'rgba(128,128,128,255)'
                step4_temp = 'rgba(128,128,128,255)'
                step5_temp = 'rgba(105,105,105,255)'
        elif ((temp_value<35.5) and (temp_value>=35)):
                step2_temp ='rgba(255,128,0,0.5)'
                step1_temp = 'rgba(105,105,105,255)'
                step4_temp = 'rgba(128,128,128,255)'
                step5_temp = 'rgba(105,105,105,255)'
        elif ((temp_value>37.5) and (temp_value<=38.3)):
                step4_temp ='rgba(255,128,0,0.5)'
                step1_temp = 'rgba(105,105,105,255)'
                step2_temp = 'rgba(128,128,128,255)'
                step5_temp = 'rgba(105,105,105,255)'
        elif  (temp_value>38.3):
                step5_temp = 'rgba(255,0,0,0.5)'
                step1_temp = 'rgba(105,105,105,255)'
                step2_temp = 'rgba(128,128,128,255)'
                step4_temp = 'rgba(128,128,128,255)'
        else:
                step1_temp = 'rgba(105,105,105,255)'
                step2_temp = 'rgba(128,128,128,255)'
                step4_temp = 'rgba(128,128,128,255)'
                step5_temp = 'rgba(105,105,105,255)'

        gaugeEData = pd.DataFrame({
                  'min':[30],
                  'level1':[35],
                  'level2':[35.5],
                  'level3':[37.5],
                  'level4':[38.3],
                  'max':[45],
                  'value':temp
                  })

        max = alt.Chart(gaugeEData).mark_bar(color=step5_temp).encode(y=alt.Y("level4:Q",scale=alt.Scale(domain=(30,45)),title=None , axis=alt.Axis(orient='right')),y2="max:Q")
        level4 = alt.Chart(gaugeEData).mark_bar(color=step4_temp).encode(y=alt.Y("level3:Q",scale=alt.Scale(domain=(30,45)),title=None , axis=alt.Axis(orient='right')),y2="level4:Q")
        level3 = alt.Chart(gaugeEData).mark_bar(color='#A9A9A9').encode(y=alt.Y("level2:Q",scale=alt.Scale(domain=(30,45)),title=None , axis=alt.Axis(orient='right')),y2="level3:Q")
        level2 = alt.Chart(gaugeEData).mark_bar(color=step2_temp).encode(y=alt.Y("level1:Q",scale=alt.Scale(domain=(30,45)),title=None , axis=alt.Axis(orient='right')),y2="level2:Q")
        level1 = alt.Chart(gaugeEData).mark_bar(color=step1_temp).encode(y=alt.Y("min:Q",scale=alt.Scale(domain=(30,45)),title=None , axis=alt.Axis(orient='right')),y2="level1:Q")
        valueLine=alt.Chart(gaugeEData).mark_bar(size=8,color='#7393B3',opacity=1).encode(y=alt.Y("min:Q",scale=alt.Scale(domain=(30,45)),title=None , axis=alt.Axis(orient='right')),y2="value:Q")

        fig_gaugeE = alt.layer(max,level4,level3,level2,level1,valueLine, width=40, height=130)
          
        gaugeE.altair_chart(fig_gaugeE)

  with imageE:

        #condition loop to change image E
        if ((temp_value>=35.5) and (temp_value<=37.5)):
                imgE = imgE_ok
        elif ((temp_value<35.5) and (temp_value>=34.5)):
                imgE = imgE_midlow
        elif ((temp_value>37.5) and (temp_value<=38.3)):
                imgE = imgE_midhigh
        elif (temp_value<34.5):
                imgE = imgE_low
        elif (temp_value>38.3):
                imgE = imgE_high
        else:
                imgE = imgE_ok
        st.image(imgE,use_column_width=True)

  with graph_E:
        temp_graph = alt.Chart(data_to_be_added).mark_line(opacity=1).encode(
                x=alt.X('time', axis=alt.Axis(title=None),scale=alt.Scale(padding=0)),
                y=alt.Y('temp', axis=alt.Axis(title=None),scale=alt.Scale(domain=[30, 45],padding=0)),
                color=alt.value("#7393B3")
                ).properties(height=125)
        
        graph_E.altair_chart(temp_graph,use_container_width=True)