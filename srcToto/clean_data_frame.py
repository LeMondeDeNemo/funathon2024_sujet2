from create_data_list import create_data_list
import pandas as pd

def clean_dataframe(df):
    df["an"] = df["ANMOIS"].astype(str).str[:4]
    df["mois"] = df["ANMOIS"].astype(str).str[-2:]

    df["mois"] = df["mois"].str.replace(r'^0+','',regex=True)

    df.colums = df.colums.str.lower()

    return df

