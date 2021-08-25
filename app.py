import streamlit as st
import pandas as pd
from pytrends.request import TrendReq

header = st.beta_container()
map_usa = st.beta_container()

with header:
    st. title('COVID statistics in the USA')
    #st. subheader('Predict the epidemiology and vaccination rate, and the anti-covid twits')
    st. text('select a state')

    imput_feature = st.text_input ('Keyword','anti-vax')

# pytrends
pytrends = TrendReq(hl='en-US')
kw_list =
cat = '0' # as string -- no subcat, 
pytrends.build_payload (kw_list ,
                 cat ,
     timeframe ='today 3-m', 
     geo='',
     gprop='')

st.write(imput_feature)

