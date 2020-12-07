import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


df= pd.read_csv("covid_impact_on_airport_traffic.csv",sep=",")

def testfile(file):
    NaN=file.isna()
    return NaN

def read_file(file):
    number = st.number_input("Selectionner un nombre de lignes")
    if(number>=5):
        st.dataframe(file.head(int(number)))
    elif(number<5):
        st.write('le nombre de ligne doit être superieur a 5')

def type_colums(file):
    st.write(file.dtypes)

def shape_df(file):
    st.write(file.shape)

def description(file):
    st.write(file.describe())

def heatmap(file):
    plt.figure(figsize=(15, 12))
    plt.title('Heatmap Impact Covid', fontsize=20)
    st.write(sb.heatmap(file.corr().astype(float).corr(), vmax=1.0, annot=True))
    st.pyplot()

def histogramme(file):
    moyenne = file.groupby('PercentOfBaseline').mean()
    moyenne['PercentOfBaseline'] = file['PercentOfBaseline'].unique()
    plt.xlabel('année')
    plt.ylabel('budget')
    plt.title('histogramme')
    sb.displot(file,x=file['PercentOfBaseline'], bins=26)
    st.pyplot()

st.write("Dataset l'impact du Covid sur le trafic aerien")
#Test du fichier
NotNull = testfile(df)
read = read_file(df)
st.write("Type des colonnes du Dataset")
type_colums(df)
st.write("Shape du Dataset")
shape_df(df)
st.write("Description du Dataset")
description(df)
st.write("heatmap")
heatmap(df)
histogramme(df)
