from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta
import os

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
        forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean,precipitation_sum,precipitation_hours&timezone=auto&start_date={today}&end_date={today}"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code != 200:
            return render_template('index.html', error = "Error fetching current weather")
        
        current_data = forecast_response.json()['daily']
        current_max = current_data['apparent_temperature_max'][0]
        current_min = current_data['apparent_temperature_min'][0]
        current_mean = current_data['apparent_temperature_mean'][0]
        current_precip_sum = current_data['precipitation_sum'][0]
        current_precip_hours = current_data['precipitation_hours'][0]

        #Historical data
        last_year_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        historical_url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={last_year_date}&end_date={last_year_date}&daily=apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean,precipitation_sum,precipitation_hours&timezone=auto"
        historical_response = requests.get(historical_url)
        if historical_response.status_code != 200:
            return render_template('index.html', error = "Error fetching historical weather")
        
        historical_data = historical_response.json()['daily']
        historical_max = historical_data['apparent_temperature_max'][0]
        historical_min = historical_data['apparent_temperature_min'][0]
        historical_mean = historical_data['apparent_temperature_mean'][0]
        historical_precip_sum = historical_data['precipitation_sum'][0]
        historical_precip_hours = historical_data['precipitation_hours'][0]

        #Comparison
        comparison = "Hotter" if current_mean > historical_mean else "Cooler" if current_mean< historical_mean else "similar"
        result = f"Today in {city}: Max: {current_max}°C, Min: {current_min}°C, Apparent Temperature (Mean): {current_mean}°C, There is expected to be {current_precip_sum}mm precipiation in {current_precip_hours} hours<br><br> This day Last year: Max: {historical_max}°C, Min: {historical_min}°C, Apparent Temperature (Mean): {historical_mean}°C, There is expected to be {historical_precip_sum}mm precipiation in {historical_precip_hours} hours<br><br><br> It's <b>{comparison}</b> today!"

        return render_template('index.html', result = result)

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    