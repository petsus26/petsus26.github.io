import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="My Multi-Source Dashboard", layout="wide")
st.title("📊 Multi-Source Data Dashboard")
st.markdown("### Replace the data loading parts with your actual sources")

# ====================== LOAD YOUR DATA HERE ======================
# Example 1: From CSV / Excel
# df_sales = pd.read_csv("sales.csv")          # or pd.read_excel("file.xlsx")

# Example 2: From API (replace with your real endpoint)
# import requests
# response = requests.get("https://api.example.com/data")
# df_api = pd.DataFrame(response.json())

# Example 3: Simulated data for testing
data1 = {
    "Date": pd.date_range("2025-01-01", periods=30),
    "Sales": [1000 + i*50 for i in range(30)],
    "Region": ["North"]*10 + ["South"]*10 + ["East"]*10
}
df = pd.DataFrame(data1)

# ====================== DASHBOARD LAYOUT ======================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Sales", f"${df['Sales'].sum():,}")
with col2:
    st.metric("Avg Daily Sales", f"${df['Sales'].mean():.0f}")
with col3:
    st.metric("Number of Days", len(df))
with col4:
    st.metric("Regions", df['Region'].nunique())

# Filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region(s)", options=df['Region'].unique(), default=df['Region'].unique())

# Filtered data
filtered_df = df[df['Region'].isin(selected_region)]

# Charts
tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Comparison", "📋 Raw Data"])

with tab1:
    fig = px.line(filtered_df, x="Date", y="Sales", color="Region", title="Sales Trend Over Time")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig2 = px.bar(filtered_df.groupby("Region")["Sales"].sum().reset_index(), 
                  x="Region", y="Sales", title="Sales by Region")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.dataframe(filtered_df, use_container_width=True)

st.caption("Built with Streamlit • Update the data loading section with your real sources")
