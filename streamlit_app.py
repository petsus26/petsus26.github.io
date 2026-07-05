import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Dashboard", layout="wide")
st.title("📊 My Multi-Source Dashboard")

# Load your data (CSV, API, database, etc.)
df1 = pd.read_csv("source1.csv")  # or API call, SQL, etc.
df2 = ... 

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Sales", "$124,560")
with col2:
    st.metric("Active Users", "3,245")

st.dataframe(df1)
# Add charts: st.line_chart(), st.bar_chart(), etc.
