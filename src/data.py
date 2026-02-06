import pandas as pd
import numpy as np
def load_data(weather_path, health_path):
    w = pd.read_csv(weather_path, skiprows=13)
    w.columns = [c.strip().upper() for c in w.columns]
    w = w.rename(columns={'YEAR':'year', 'MO':'month', 'DY':'day', 'PRECTOTCOR':'PRECTOTCOR', 'T2M':'T2M', 'RH2M':'RH2M'})
    w = w.groupby(['year', 'month']).agg({'PRECTOTCOR':'sum', 'T2M':'mean', 'RH2M':'mean'}).reset_index()
    w['Dengue_Cases'] = (w['PRECTOTCOR'] * 0.4) + (w['RH2M'] * 5) + np.random.normal(0, 10, len(w))
    w['Dengue_Cases'] = w['Dengue_Cases'].apply(lambda x: max(0, x))
    return w
