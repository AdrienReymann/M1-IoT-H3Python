import streamlit as st
import pandas as pd
import numpy as np

def  loadfile():
    covid = pd.read_csv("covid_impact_on_airport_traffic.csv",sep=",")
    return covid

df = loadfile()
st.write(df)

def testfile(file):
    NaN=file.isna()
    return NaN

NotNull = testfile(df)
st.write(NotNull)



