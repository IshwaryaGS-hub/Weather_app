from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "bb2727581770683adf255d1a687f5ec6"   

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return render_template("weather.html", error="No city provided.")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"

    response = requests.get(url).json()

    if response.get("cod") != 200:
        return render_template("weather.html", error="City not found")

    data = {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "wind": response["wind"]["speed"],
        "description": response["weather"][0]["description"].title(),
        "icon": response["weather"][0]["icon"]
    }

    return render_template("weather.html", data=data)
    

if __name__ == "__main__":
    app.run(debug=True)
