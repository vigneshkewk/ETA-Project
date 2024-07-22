import streamlit as st
import pandas as pd
import sklearn 
from sklearn.linear_model import LinearRegression
import pickle

model = pickle.load(open("estimator.pkl",'rb'))
start_lat = st.number_input("Enter the star lattitude:")
start_lang = st.number_input("Enter the star longitude:")
end_lat = st.number_input("Enter the dest lattitude:")
end_lang = st.number_input("Enter the end longitude:")
dist = st.number_input("Enter the distance:")
density = st.number_input("Enter the density:")
weather = st.number_input("Enter the star lat:")
day  = st.number_input("Enter the day:")
hour = st.number_input("Enter the hour:")

weather_numerical = 1 if weather == "rainy" else 2 if weather=='foggy' else 3


if st.button("Submit"):
    time = model.predict([[start_lat,start_lang ,end_lat,end_lang,dist,density,weather_numerical,day,hour]])[0]
    st.write("The Estimated time is",time,'minutes')
