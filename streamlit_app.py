import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime

st.set_page_config(page_title="Multi-Source Dashboard", layout="wide")
st.title("📊 Multi-Source Dashboard")
st.markdown(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# ====================== DATABASE CONNECTION ======================
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host="YOUR_HOST",           # e.g. localhost or your Postgres server
        database="YOUR_DATABASE_NAME",
        user="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        port="5432"                 # usually 5432
    )

# ====================== LOAD DATA FROM POSTGRES ======================
def load_data(table_name):
    conn = get_connection()
    query = f"SELECT * FROM {table_name} LIMIT 10000"   # adjust LIMIT as needed
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Load data from your tables (change table names to match yours)
try:
    df_ig = load_data("instagram_data")          # ← change to your actual table name
    df_fb = load_data("facebook_data")
    df_tiktok = load_data("tiktok_data")
    df_yt = load_data("youtube_data")
    df_mailchimp = load_data("mailchimp_data")
    df_whatsapp = load_data("whatsapp_data")
    df_ga = load_data("google_analytics")
    df_gads = load_data("google_ads")
    
    st.success("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    st.error(f"Connection error: {e}")
    st.info("Using sample data for now...")
    # Fallback sample data
    dates = pd.date_range(start="2025-01-01", periods=60, freq="D")
    data = {"Date": dates, "Impressions": [5000 + i*10 for i in range(60)], "Clicks": [300 + i for i in range(60)]}
    df_ig = df_fb = df_tiktok = df_yt = df_mailchimp = df_whatsapp = df_ga = df_gads = pd.DataFrame(data)

# ====================== TABS ======================
tab_instagram, tab_facebook, tab_tiktok, tab_youtube, tab_mailchimp, tab_whatsapp, tab_ga, tab_gads = st.tabs([
    "📸 Instagram", "👍 Facebook", "🎵 TikTok", "📺 YouTube",
    "✉️ Mailchimp", "💬 WhatsApp Business", "📊 Google Analytics", "💰 Google Ads"
])

with tab_instagram:
    st.subheader("Instagram Performance")
    st.line_chart(df_ig.set_index("Date")[["Impressions", "Clicks"]] if "Date" in df_ig.columns else df_ig)

with tab_facebook:
    st.subheader("Facebook Performance")
    st.bar_chart(df_fb)

with tab_tiktok:
    st.subheader("TikTok Performance")
    st.line_chart(df_tiktok)

with tab_youtube:
    st.subheader("YouTube Performance")
    st.bar_chart(df_yt)

with tab_mailchimp:
    st.subheader("Mailchimp Performance")
    st.line_chart(df_mailchimp)

with tab_whatsapp:
    st.subheader("WhatsApp Business API")
    st.bar_chart(df_whatsapp)

with tab_ga:
    st.subheader("Google Analytics")
    st.line_chart(df_ga)

with tab_gads:
    st.subheader("Google Ads")
    st.bar_chart(df_gads)

st.caption("Data from Airbyte → PostgreSQL")
