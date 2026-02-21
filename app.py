import streamlit as st
import pandas as pd
import os
from src.data import load_data
from src.model import get_model
st.set_page_config(page_title="Vecto Shield", layout="wide")
df = load_data(os.path.join("Data", "pune_weather.csv"), os.path.join("Data", "pune_health.csv"))
model = get_model(df)
st.success("System Operational")
