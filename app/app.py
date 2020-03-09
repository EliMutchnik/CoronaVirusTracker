from flask import Flask, render_template
import requests, json

app = Flask(__name__)
URL = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query?f=json&where=Confirmed%20%3E%200&outFields=*'

# Collect the updated data on CoronaVirus countries
def get_data():
    req = requests.get(url=URL) 
    return req.json()['features']

# Build data list
def build_list(countries):
    return [
        {
            'name': country['attributes']['Country_Region'],
            'confirmed': country['attributes']['Confirmed'],
            'deaths': country['attributes']['Deaths'],
            'recovered': country['attributes']['Recovered']
        }
        for country in countries
        if country['attributes']['Country_Region'] != 'Others'
    ]

# Return sorted list of top 10 countries with most confirmed cases
def get_top(data):
    confirmed_countries = sorted(data, key = lambda item: item['attributes']['Confirmed'], reverse=True)
    return build_list(confirmed_countries)[:10]

# Return alphabetically sorted list of all countries with confirmed cases
def get_all(data):
    all_countries = sorted(data, key = lambda item: item['attributes']['Country_Region'])
    return build_list(all_countries)

@app.route('/', methods=['GET'])
def health_check():
    return "Welcome to the Corona Virus Tracker!<br />(please don't sneeze on me...)"

@app.route('/all', methods=['GET'])
def all_countries():
    data = get_data()
    return render_template('main.html', countries=get_all(data))

@app.route('/top', methods=['GET'])
def top_countries():
    data = get_data()
    return render_template('main.html', countries=get_top(data))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)