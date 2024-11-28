from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_KEY = 'f00c38e0279b7bc85480c3fe775d518c'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city_name = request.form['city']
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'name': data['name'],
            'temp': f"{data['main']['temp']}°C",
            'description': data['weather'][0]['description'],
            'wind_speed': f"Wind Speed: {data['wind']['speed']} m/s",
            'date': data['dt']
        })
    return jsonify({'error': 'City not found. Please try again.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
