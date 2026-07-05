import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Multi-Source Dashboard", layout="wide")
st.title("📊 Multi-Source Dashboard")
st.markdown(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Sample data (you can customize later)
dates = pd.date_range(start="2025-01-01", periods=60, freq="D")

base_data = {
    "Date": dates,
    "Impressions": [5000 + (i % 10)*300 for i in range(60)],
    "Clicks": [300 + (i % 10)*25 for i in range(60)],
    "Conversions": [45 + (i % 7)*3 for i in range(60)],
    "Spend": [120 + (i % 10)*15 for i in range(60)]
}

df = pd.DataFrame(base_data)

# Platform tabs
tab_instagram, tab_facebook, tab_tiktok, tab_youtube, tab_mailchimp, tab_whatsapp, tab_ga, tab_gads = st.tabs([
    "📸 Instagram",
    "👍 Facebook",
    "🎵 TikTok",
    "📺 YouTube",
    "✉️ Mailchimp",
    "💬 WhatsApp Business",
    "📊 Google Analytics",
    "💰 Google Ads"
])

# Common metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Impressions", f"{df['Impressions'].sum():,}")
with col2:
    st.metric("Total Clicks", f"{df['Clicks'].sum():,}")
with col3:
    st.metric("Total Conversions", f"{df['Conversions'].sum():,}")
with col4:
    st.metric("Total Spend", f"${df['Spend'].sum():,}")

# ====================== PLATFORM TABS ======================

with tab_instagram:
    st.subheader("Instagram Performance")
    st.line_chart(df.set_index("Date")[["Impressions", "Clicks"]], use_container_width=True)
    st.dataframe(df.head(10), use_container_width=True)

with tab_facebook:
    st.subheader("Facebook Performance")
    st.bar_chart(df.set_index("Date")["Conversions"])
    st.dataframe(df.head(10), use_container_width=True)

with tab_tiktok:
    st.subheader("TikTok Performance")
    st.line_chart(df.set_index("Date")["Impressions"], use_container_width=True)
    st.dataframe(df.head(10), use_container_width=True)

with tab_youtube:
    st.subheader("YouTube Performance")
    st.bar_chart(df.set_index("Date")["Clicks"])
    st.dataframe(df.head(10), use_container_width=True)

with tab_mailchimp:
    st.subheader("Mailchimp Performance")
    st.line_chart(df.set_index("Date")["Conversions"], use_container_width=True)
    st.dataframe(df.head(10), use_container_width=True)

with tab_whatsapp:
    st.subheader("WhatsApp Business API")
    st.metric("Messages Sent", "12,458")
    st.metric("Response Rate", "68%")
    st.bar_chart(df.set_index("Date")["Conversions"])
    st.dataframe(df.head(10), use_container_width=True)

with tab_ga:
    st.subheader("Google Analytics")
    st.line_chart(df.set_index("Date")[["Impressions", "Clicks"]], use_container_width=True)
    st.dataframe(df.head(10), use_container_width=True)

with tab_gads:
    st.subheader("Google Ads")
    st.bar_chart(df.set_index("Date")["Spend"])
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("ROAS", "4.8x")
    with col_b:
        st.metric("Cost per Conversion", "$18.40")
    st.dataframe(df.head(10), use_container_width=True)

st.caption("Multi-Platform Dashboard • Built with Streamlit")