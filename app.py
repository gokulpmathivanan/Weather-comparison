from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if not city: 
            return render_template('index.html', error = "Please enter a city.")

        #Geocode
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geocode_response = requests.get(geocode_url)
        if geocode_response.status_code != 200 or not geocode_response.json().get('results'):
            return render_template('index.html', error = "City not found")
        result = geocode_response.json()['results'][0]
        latitude = result['latitude']
        longitude = result['longitude']

        #Forecast API
        today = datetime.now().strftime('%Y-%m-%d')
        forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=auto&start_date={today}&end_date={today}"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code != 200:
            return render_template('index.html', error = "Error fetching current weather")
        
        current_data = forecast_response.json()['daily']
        current_max = current_data['temperature_2m_max'][0]
        current_min = current_data['temperature_2m_min'][0]


        return render_template('index.html', result = "Weather will appear here")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)
    