# Weather comparison (Work in Progress)

A simple tool to know what the weather was like last year compared to the current date
<img width="405" height="242" alt="image" src="https://github.com/user-attachments/assets/1b85a264-fa98-4041-b2c1-b2b4be186f80" />

Check it out here: https://weather-comparison-z4uh.onrender.com/

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
