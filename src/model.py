import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from src.config import MODEL_PATH
def get_model(df):
    if os.path.exists(MODEL_PATH):
        try: return joblib.load(MODEL_PATH)
        except Exception: pass
    X, y = df[['PRECTOTCOR', 'T2M', 'RH2M']], df['Dengue_Cases']
    model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model
