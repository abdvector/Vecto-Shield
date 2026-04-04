import streamlit as st
def inject_custom_css():
    st.markdown("""
    <style>
        .stApp { background-color: #090c15; color: #e2e8f0; }
        .stTabs [data-baseweb="tab-list"] { gap: 10px; }
        .stTabs [data-baseweb="tab"] { background-color: #1e293b; border-radius: 4px; padding: 10px 20px; color: white; border: 1px solid #334155; }
        .stTabs [aria-selected="true"] { background-color: #064e3b !important; border-color: #10b981 !important; border-bottom: 2px solid #10b981 !important; }
        div[data-testid="stMetricValue"] { color: #10b981; }
    </style>
    """, unsafe_allow_html=True)
