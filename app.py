import streamlit as st
import pandas as pd
from pytrends.request import TrendReq

header = st.container()
map_usa = st.container()

with header:
    st. title('Predict Beer preference in Indiana')
    #st. subheader('Predict taste')
    st. text('select a state')

    imput_feature = st.text_input ('Keyword','anti-vax')

# pytrends
pytrends = TrendReq(hl='en-US')
kw_list = imput_feature
cat = '0' # as string -- no subcat, 
pytrends.build_payload (kw_list ,
                 cat ,
     timeframe ='today 3-m', 
     geo='',
     gprop='')

st.write(imput_feature)



# hide burger and footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
