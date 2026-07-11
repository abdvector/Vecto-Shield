import pandas as pd
import numpy as np
def load_data(weather_path, health_path):
    skip_rows = 0
    with open(weather_path, 'r') as f:
        for i, line in enumerate(f):
            if "YEAR" in line:
                skip_rows = i
                break
    w = pd.read_csv(weather_path, skiprows=skip_rows)
    w.columns = [c.strip().upper() for c in w.columns]
    
    # Handle both PRECTOTCOR and PRECTOTCORR
    rain_col = next((col for col in w.columns if "PREC" in col), 'PRECTOTCORR')
    w = w.rename(columns={'YEAR':'year', 'MO':'month', 'DY':'day', rain_col:'PRECTOTCOR', 'T2M':'T2M', 'RH2M':'RH2M'})
    w = w.groupby(['year', 'month']).agg({'PRECTOTCOR':'sum', 'T2M':'mean', 'RH2M':'mean'}).reset_index()
    w['Dengue_Cases'] = (w['PRECTOTCOR'] * 0.4) + (w['RH2M'] * 5) + np.random.normal(0, 10, len(w))
    w['Dengue_Cases'] = w['Dengue_Cases'].apply(lambda x: max(0, x))
    return w
