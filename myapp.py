from tkinter import Variable
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import plotly.figure_factory as ff
from matplotlib import pyplot as plt


st.set_page_config(page_title='Survey Results')
st.header('Stoppage Analysis MINE-II DEC 2022')

#load dataframe
excel_file = 'MII.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(excel_file,sheet_name=sheet_name,usecols='I:T')
df.head()

#streamlit selection

secs = df['secs'].tolist()
secs_selection =[7532100,
 6208200,
 4976700,
 4605300,
 4154100,
 3938700,
 3018300,
 2883600,
 2783700,
 2707200]
stopcode = df['stopcode'].tolist()
stopcode_selection =['4409',
 '3002',
 '0721',
 '0799',
 '1012',
 '0901',
 '1001',
 '9404',
 '4501',
 '3301']
Groupcodetext = df['Group code text'].tolist()
Groupcodetext_selection=['Conveyor Vulcanising',
 'Planned Operation',
 'Common Miscellaneous',
 'Common Miscellaneous',
 'BWE Operation',
 'Common Other',
 'BWE Operation',
 'Unplanned Vulcanising',
 'Conveyor CMM',
 'Planned SME OH'] 
Causecodetext = df['Cause code text'].tolist()
Causecodetext_selection =['BTR Clamp fixing',
 'Daily maintenance',
 'Machine on Stand-By',
 'Others',
 'BWE Repostioning/movement',
 'OB Rear load',
 'BWE Track Area Preparation',
 'Conveyor unplanned vulcanising',
 'Line  roller changing/removal',
 'Over haul']
  
# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['secs'].isin(secs_selection)) & (df['stopcode'].isin(stopcode_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

mask = (df['Group code text'].isin(Groupcodetext_selection)) & (df['Cause code text'].isin(Causecodetext_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION

df_grouped = df[mask].groupby(by=['Cause code text']).count()[['secs']]
df_grouped = df_grouped.rename(columns={'secs': 'Hours'})
df_grouped = df_grouped.reset_index()

bar_chart = px.bar(df_grouped,
                   x='Cause code text',
                   y='Hours',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)



# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Group code text']).count()[['secs']]
df_grouped = df_grouped.rename(columns={'secs': 'hours'})
df_grouped = df_grouped.reset_index()

bar_chart = px.bar(df_grouped,
                   x='Group code text',
                   y='hours',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)



