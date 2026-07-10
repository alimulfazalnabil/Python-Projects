import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌤️ Weather Dashboard")

API_KEY = "YOUR_API_KEY_HERE"  # Get from OpenWeatherMap

city = st.text_input("Enter city name", value="London")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", f"{data['main']['temp']}°C")
        col2.metric("Humidity", f"{data['main']['humidity']}%")
        col3.metric("Wind Speed", f"{data['wind']['speed']} m/s")
        
        st.write(f"**Weather:** {data['weather'][0]['description'].title()}")
    else:
        st.error("City not found. Try another search.")
