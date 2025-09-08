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

        return render_template('index.html', results = "Weather will appear here.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)
    