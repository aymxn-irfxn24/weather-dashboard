import streamlit as st 
import pandas as pd 
import requests 
import numpy as np

st.title("The Weather Dashboard")
def add_bg():
    st.markdown(
    f"""
        <style>
        .stApp{{
        background-image: url("https://images.pexels.com/photos/851151/pexels-photo-851151.jpeg?auto=compress&cs=tinysrgb&w=600");
        background-size: cover;
        background-position: center;
        background-attachment:fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()

cmb = requests.get("https://api.open-meteo.com/v1/forecast?latitude=6.9355&longitude=79.8487&daily=temperature_2m_min,temperature_2m_max,rain_sum&current=temperature_2m,is_day,rain,precipitation,showers,snowfall,weather_code")
kandy=requests.get("https://api.open-meteo.com/v1/forecast?latitude=7.2906&longitude=80.6336&daily=temperature_2m_min,temperature_2m_max,rain_sum&current=temperature_2m,precipitation,rain,showers,snowfall,weather_code")
nyc=requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&daily=temperature_2m_min,temperature_2m_max,rain_sum&current=temperature_2m,precipitation,rain,showers,snowfall,weather_code")
shanghai=requests.get("https://api.open-meteo.com/v1/forecast?latitude=31.2222&longitude=121.4581&daily=temperature_2m_min,temperature_2m_max,rain_sum&current=temperature_2m,precipitation,rain,showers,snowfall,weather_code")
rome=requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.8919&longitude=12.5113&daily=temperature_2m_min,temperature_2m_max,rain_sum&current=temperature_2m,precipitation,rain,showers,snowfall,weather_code")
option = st.sidebar.selectbox(
    "Cities",
    ["Colombo","Kandy","New York","Shanghai","Rome"]
)

if option == "Colombo":
    resp=cmb

elif option == "Kandy":
    resp=kandy

elif option == "New York":
    resp=nyc

elif option=="Shanghai":
    resp=shanghai

else :
    resp = rome


value=resp.json()

if "current" in value:
    temp= value["current"]["temperature_2m"]
    rain= value["current"].get("rain",0)
    prs=  value["current"]["precipitation"]
    shower= value["current"]["showers"]
    snow = value["current"]["snowfall"]

if rain > 0 :
    weather_condition= "Rainy"
    st.image("https://cdn-icons-png.freepik.com/256/3262/3262916.png?ga=GA1.1.1068603687.1693735616&semt=ais_hybrid")
    st.caption("Rainy right now")
if snow>0 :
    st.image("https://cdn-icons-png.freepik.com/256/5977/5977559.png?ga=GA1.1.1068603687.1693735616&semt=ais_hybrid")
    st.caption("Snowy right now")
    st.snow()
else :
    weather_condition="Sunny"
    st.image("https://cdn-icons-png.freepik.com/256/1710/1710829.png?ga=GA1.1.1068603687.1693735616&semt=ais_hybrid")
    st.caption("Sunny right now")

# st.markdown(f"{weather_condition}")
# st.metric("Temprature",value=temp)
# st.metric("Rainfall",value=rain)
# st.metric("Precipitation",value=prs)
# st.metric("Showers",value=shower)

col1, col2, col3, col4,col5 = st.columns(5)
col1.metric("Temperature(°C)🌡️", value=temp,)
col2.metric("Wind(km/ph)🍃", value=rain,)
col3.metric("Humidity(%)",value=prs)
col4.metric("Rainfall(mm)🌧️",value=rain)
col5.metric("Snowfall(cm)❄️",value=snow)


# st.sidebar.caption("You have selected:", option)

if option== "Colombo":
    st.sidebar.image("https://images.pexels.com/photos/2239999/pexels-photo-2239999.jpeg?auto=compress&cs=tinysrgb&w=600")
if option=="Kandy":
    st.sidebar.image("https://images.pexels.com/photos/739409/pexels-photo-739409.jpeg?auto=compress&cs=tinysrgb&w=600")
if option=="New York":
    st.sidebar.image("https://images.pexels.com/photos/1486222/pexels-photo-1486222.jpeg?auto=compress&cs=tinysrgb&w=600")
if option=="Shanghai":
    st.sidebar.image("https://images.pexels.com/photos/2598623/pexels-photo-2598623.jpeg?auto=compress&cs=tinysrgb&w=600")
if option=="Rome": 
    st.sidebar.image("https://images.pexels.com/photos/2064827/pexels-photo-2064827.jpeg?auto=compress&cs=tinysrgb&w=600")



daily_temp=pd.DataFrame(value["daily"]["temperature_2m_max"],
                        value["daily"]["time"])

st.line_chart(daily_temp)
st.caption("7 day Prediction of Temprature")

# st.video("https://videocdn.cdnpk.net/videos/a4998f65-1be7-524f-81c9-5c22384cc376/horizontal/previews/clear/small.mp4?token=exp=1745680142~hmac=20cf67005ec9bce4c334c2c52630e5076ea2e65b232201b1d40afe0212d91f01")

