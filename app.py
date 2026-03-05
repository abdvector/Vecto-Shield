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
        heatmap = pdk.Layer("HeatmapLayer", data=target_df, get_position="[lon, lat]", get_weight="weight", radiusPixels=50, intensity=1)
        st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/dark-v10', initial_view_state=pdk.ViewState(longitude=patna_center[0], latitude=patna_center[1], zoom=11.5, pitch=0), layers=[heatmap]))
