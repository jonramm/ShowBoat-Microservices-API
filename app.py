import os
from flask import Flask, request, jsonify
import requests
import pprint

app = Flask(__name__)

@app.route("/artist-search", methods=['GET', 'POST'])
def artist_search():
    """
    Artist search endpoint which takes a search string from the body of a POST request and uses
    it to call The AudioDB artist search API endpoint. Returns a custom JSON return object with
    data for the app.
    """
    if request.method == 'POST':
        url = f"https://www.theaudiodb.com/api/v1/json/{os.getenv('AUDIODB_API_KEY')}/search.php?s={request.form.get('artist_search')}"
        response = requests.get(url)
        data = response.json()
        # if we find an artist in the db we create a return object with pertinent data
        if data['artists']:
            obj = {
                'artist': data['artists'][0]['strArtist'],
                'bio': data['artists'][0]['strBiographyEN'],
                'img_url': data['artists'][0]['strArtistThumb'],
                'website': data['artists'][0]['strWebsite'],
                'id': data['artists'][0]['idArtist']
            }
        else:
            # if no artist is found in db
            obj = {
                'artist': None
            }
        return obj


@app.route("/tour-search", methods=['GET', 'POST'])
def tour_search():
    """
    Tour search endpoint which takes a search string from the body of a POST request and uses
    it to call the Songkick API artist search endpoint to find the artist ID, then uses that
    ID to call the Songkick API artist calendar endpoint. Returns a JSON return object 
    containing a list of event objects, if any.
    """
    if request.method == 'POST':
        id_url = f"https://api.songkick.com/api/3.0/search/artists.json?apikey={os.getenv('SONGKICK_API_KEY')}&query={request.form.get('artist_search')}"
        response = requests.get(id_url)
        id_data = response.json()
        id = id_data['resultsPage']['results']['artist'][0]['id']
        tour_url = f"https://api.songkick.com/api/3.0/artists/{id}/calendar.json?apikey={os.getenv('SONGKICK_API_KEY')}"
        response = requests.get(tour_url)
        tour_data = response.json()
        # if we get tour data from db
        if tour_data['resultsPage']['results']:
            events = tour_data['resultsPage']['results']['event']
        # if no tour data, return empty list
        else:
            events = []
        obj = {
            'events': events
        }
        return obj
        

@app.route("/video-search", methods=['GET', 'POST'])
def video_search():
    """
    Video search endpoint which takes an artist ID string from the body of a POST request and uses
    it to call The AudioDB API video search endpoint. Returns a JSON return object containing a
    maximum od three YouTube urls for display in the app. 
    """
    if request.method == 'POST':
        url = f"https://theaudiodb.com/api/v1/json/2/mvid.php?i={request.form.get('artist_id')}"
        response = requests.get(url)
        data = response.json()
        video_urls = []
        # if there are video urls available
        if data['mvids']:
            numVids = len(data['mvids'])
            # if there are less than three urls, set the for loop range variable to that number
            if numVids < 3:
                indexes = numVids
            else:
                indexes = 3
        else:
            indexes = 0
        for i in range(indexes):
            if data['mvids']:
                video_urls.append(data['mvids'][i]['strMusicVid'])
        obj = {
            'video_urls': video_urls
        }
        return obj

@app.route("/caffeine", methods=['GET', 'POST'])
def caffeine():
    """
    """
    if request.method == 'POST':
        weight = request.form.get('weight')
        caffeine = request.form.get('caffeine')
        res = caffeine_safety(weight, caffeine)
        obj = {"limit": res}
        return obj

@app.route("/", methods=['GET'])
def hello():
    return "Hello world!"

def caffeine_safety(weight, caffeine):
    pass

if __name__ == '__main__':
    p = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=p, host='0.0.0.0')