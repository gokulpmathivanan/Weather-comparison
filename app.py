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

        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geocode_response = requests.get(geocode_url)
        if geocode_response.status_code != 200 or not geocode_response.json().get('results'):
            return render_template('index.html', error = "City not found")
        result = geocode_response.json()['results'][0]
        latitude = result['latitude']
        longitude = result['longitude']

        return render_template('index.html', result = "Weather will appear here.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)
    