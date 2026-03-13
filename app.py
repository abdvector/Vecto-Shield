import streamlit as st
import pandas as pd
import os
import pydeck as pdk
from src.data import load_data
from src.model import get_model
from src.ui_components import inject_custom_css

st.set_page_config(page_title="Vecto Shield", layout="wide", initial_sidebar_state="collapsed")
inject_custom_css()
df = load_data(os.path.join("Data", "pune_weather.csv"), os.path.join("Data", "pune_health.csv"))
model = get_model(df)
tab1, tab2, tab3 = st.tabs(["1 HOTSPOT MAP", "2 DRONE OPERATIONS", "3 ANALYTICS DASHBOARD"])

with tab1:
    col_map, col_side = st.columns([2, 1])
    with col_map:
        st.subheader("LIVE RISK HEATMAP")
        patna_center = [85.1376, 25.5941]
        target_df = pd.DataFrame([ [85.12, 25.60, 0.92], [85.15, 25.58, 0.87], [85.10, 25.59, 0.81], [85.14, 25.61, 0.76], [85.16, 25.57, 0.73] ], columns=['lon', 'lat', 'weight'])
        heatmap = pdk.Layer("HeatmapLayer", data=target_df, get_position="[lon, lat]", get_weight="weight", radiusPixels=80, intensity=1, colorRange=[[0,255,0],[255,255,0],[255,0,0]])
        st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/dark-v10', initial_view_state=pdk.ViewState(longitude=patna_center[0], latitude=patna_center[1], zoom=12, pitch=0), layers=[heatmap]))
    with col_side:
        st.subheader("TOP 5 HIGH RISK CLUSTERS")
        cluster_df = pd.DataFrame({
            "Rank": [1, 2, 3, 4, 5],
            "Cluster / Area": ["Kankarbagh", "Rajendra Nagar", "Kumhrar", "Patliputra", "Gulzarbagh"],
            "Risk Score": ["0.92 (Critical)", "0.87 (High)", "0.81 (High)", "0.76 (High)", "0.73 (High)"],
            "Predicted Cases": [152, 128, 111, 102, 95]
        })
        st.dataframe(cluster_df, hide_index=True, use_container_width=True)

        st.divider()
        st.subheader("CURRENT CONDITIONS (PATNA)")
        c1, c2, c3 = st.columns(3)
        c1.metric("Temperature", "29.1 °C")
        c2.metric("Humidity", "74 %")
        c3.metric("Rainfall (24h)", "12.4 mm")
        
        st.error("AI Prediction (14-Day): **HIGH RISK**\n\nRecommended Action: Deploy Drone Squadrons")
