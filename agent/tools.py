import pandas as pd

def load_data():
    df = pd.read_csv("data/jobs.csv")
    return df

def analyze_salary():
    df = load_data()
    return df.groupby("role")["salary"].mean().to_string()
