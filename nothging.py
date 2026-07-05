import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Basic page setup
st.set_page_config(page_title="Basic Dashboard", layout="wide")
st.title("📊 Basic Data Dashboard")
st.markdown(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# ====================== SAMPLE DATA ======================
# You can replace this later with your real data
data = {
    "Date": pd.date_range(start="2025-01-01", periods=60, freq="D"),
    "Sales": [1200, 1350, 1100, 1450, 1600, 1550, 1700] * 8 + [1800, 1900],
    "Region": ["North"]*20 + ["South"]*20 + ["East"]*20,
    "Category": ["Electronics"]*15 + ["Clothing"]*15 + ["Home"]*15 + ["Books"]*15,
    "Profit": [240, 270, 220, 290, 320, 310, 340] * 8 + [360, 380]
}

df = pd.DataFrame(data)

# ====================== METRICS ======================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Sales", f"${df['Sales'].sum():,}")
with col2:
    st.metric("Total Profit", f"${df['Profit'].sum():,}")
with col3:
    st.metric("Avg Daily Sales", f"${df['Sales'].mean():.0f}")
with col4:
    st.metric("Number of Records", len(df))

# ====================== FILTERS ======================
st.sidebar.header("Filters")
selected_regions = st.sidebar.multiselect("Region", options=df["Region"].unique(), default=df["Region"].unique())
selected_categories = st.sidebar.multiselect("Category", options=df["Category"].unique(), default=df["Category"].unique())

# Apply filters
filtered_df = df[
    (df["Region"].isin(selected_regions)) & 
    (df["Category"].isin(selected_categories))
]

# ====================== CHARTS ======================
tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Breakdown", "📋 Data Table"])

with tab1:
    fig1 = px.line(filtered_df, x="Date", y="Sales", color="Region", 
                   title="Sales Trend Over Time")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    col_a, col_b = st.columns(2)
    with col_a:
        fig2 = px.bar(filtered_df.groupby("Category")["Sales"].sum().reset_index(),
                      x="Category", y="Sales", title="Sales by Category")
        st.plotly_chart(fig2, use_container_width=True)
    with col_b:
        fig3 = px.pie(filtered_df.groupby("Region")["Profit"].sum().reset_index(),
                      names="Region", values="Profit", title="Profit by Region")
        st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.dataframe(filtered_df.sort_values("Date", ascending=False), use_container_width=True)

st.caption("Basic Streamlit Dashboard • Share this file or deploy it online")
