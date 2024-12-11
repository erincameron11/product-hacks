# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import pandas as pd


# ------------------------------------ MAIN APP ------------------------------------
# Change the title and favicon of the app in the browser
st.set_page_config(layout='wide', page_title='Product Hacks', page_icon=":sparkles:")

st.title(':sparkles: Product Hacks')

st.write(f'*Disclaimer: The products listed here are based on recommendations from TikTok creator [Nina Pool](https://www.tiktok.com/@ninaghoulina)*')

st.divider()

# Read in the database and drop the TikTok video link column
df = pd.read_csv('data.csv')
df = df.drop('TikTok Reference Video', axis=1)

# Locate the number of rows to calculate the height of the dataframe needed
n_rows = df.shape[0]
df_height = (n_rows + 1) * 35 + 3

# Display the dataframe
st.dataframe(df, height=df_height, width=2000)