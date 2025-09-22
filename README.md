# Weather comparison (Work in Progress)

A simple tool to know what the weather was like last year compared to the current date. The app retrieves current and historical weather data from Open-Meteo to enable such a comparison. Only the apparent temperature is included i.e., the temperature perceived by us (a function of actual temperature, windchill factor, relative humidity and solar radiation) and not the actual temperature itself.

<div align="center">
<img width="435" height="550" alt="image" src="https://github.com/user-attachments/assets/84bbe3c0-e908-434e-9b25-2c96cb595f94" />
</div>


Check it out here: https://weather-comparison-z4uh.onrender.com/

<ins>Note</ins>: The website may take a while to load when opening for the first time (and thereafter if left unused for more than 15 minutes). This is a limitation of the free version of render.com

## How to run locally
1. Clone the repo: `git clone https://github.com/gokulpmathivanan/Weather-comparison.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open `http://127.0.0.1:5000/` in a browser.

Framework:
- Python, Flask
- Open-Meteo APIs (Geocoding, Forecast, Historical)
- Git/GitHub for version control
- Render for deployment
