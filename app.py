import streamlit as st
import pandas as pd
import os
from src.data import load_data
from src.model import get_model
st.set_page_config(page_title="Vecto Shield", layout="wide", initial_sidebar_state="collapsed")
df = load_data(os.path.join("Data", "pune_weather.csv"), os.path.join("Data", "pune_health.csv"))
model = get_model(df)
tab1, tab2, tab3 = st.tabs(["1 HOTSPOT MAP", "2 DRONE OPERATIONS", "3 ANALYTICS DASHBOARD"])
with tab1: st.header("Hotspot Map")
with tab2: st.header("Drone Operations")
with tab3: st.header("Analytics")
