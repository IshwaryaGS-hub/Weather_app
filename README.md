## 🌦️ Weather App

A simple and beautiful Weather Application built using Flask, TailwindCSS, and the OpenWeatherMap API.
This app allows users to search for real-time weather data by entering any city name.

## Live Demo
🔗 Live Weather App on Render:
👉 https://weather-app-ofqz.onrender.com

 ## Features

  Search weather by city name
  Shows temperature, humidity, wind speed
  Shows real weather icons from OpenWeather
  Clean UI with TailwindCSS
  Flask backend
  Error handling (invalid city, API failures)
  Fully deployed using Render


#  Tech Stack
  Frontend -
  HTML5
  
  TailwindCSS
  
  Custom CSS Effects
  
  Backend- Python Flask
  
  API - OpenWeatherMap API

 Deployment - Render 

---------

## Setup & Installation
1️⃣ Clone the repository
git clone <your-repo-link>
cd weather-app

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate it

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run the project
python app.py


Open in browser:
👉 http://127.0.0.1:5000/

🌐 Deployment on Render

This project is deployed using Render Web Service with the following configuration:

render.yaml
services:
  - type: web
    name: weather-app
    runtime: python
    region: oregon
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    plan: free

You can deploy your own fork by connecting the GitHub repo to Render.

##  Environment Variables

Create a .env file (if using API key locally):

API_KEY=your_openweather_api_key


In Flask:

import os
api_key = os.getenv("API_KEY")

-------

## Note 
If you like this project, please ⭐ star the repo on GitHub — it helps a lot!

Developed by __galwhocodes__ | Ishwarya | FullStack Developer
