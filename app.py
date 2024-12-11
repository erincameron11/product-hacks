# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import pandas as pd


# ------------------------------------ MAIN APP ------------------------------------
# Change the title and favicon of the app in the browser
st.set_page_config(layout='wide', page_title='Product Hacks', page_icon=":sparkles:")

st.title(':sparkles: Product Hacks')

st.write(f'*Disclaimer: The products listed here are based on recommendations from TikTok creator [Nina Pool](https://www.tiktok.com/@ninaghoulina)*')

st.divider()

df = pd.read_csv('data.csv')
df = df.drop('TikTok Reference Video', axis=1)

st.dataframe(df, height=600, width=2000)