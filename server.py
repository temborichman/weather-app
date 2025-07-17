from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'Bulawayo')
    weather_data = get_current_weather(city)
    return render_template('weather.html', weather=weather_data, city=city)


if __name__ == "__main__":
    serve(app, host="0.0.0.0",port=8000)