import os
from flask import Flask, request, send_file, render_template
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/artist-search", methods=['GET', 'POST'])
def artist_search():
    """
    Artist search endpoint which takes a search string from the body of a POST request and uses
    it to call The AudioDB artist search API endpoint. Returns a custom JSON return object with
    data for the app.
    """
    if request.method == 'POST':
        url = f"https://www.theaudiodb.com/api/v1/json/{os.environ.get('AUDIODB_API_KEY')}/search.php?s={request.form.get('artist_search')}"
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
        id_url = f"https://api.songkick.com/api/3.0/search/artists.json?apikey={os.environ.get('SONGKICK_API_KEY')}&query={request.form.get('artist_search')}"
        response = requests.get(id_url)
        id_data = response.json()
        id = id_data['resultsPage']['results']['artist'][0]['id']
        tour_url = f"https://api.songkick.com/api/3.0/artists/{id}/calendar.json?apikey={os.environ.get('SONGKICK_API_KEY')}"
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

@app.route("/image-transform", methods=['GET', 'POST'])
def image_transform():
    """
    Image transform endpoint that takes an image url, height, and width in the body of a
    POST request and returns a JPEG file with that image with the specified dimensions. 
    Image is transformed into a thumbnail version of itself which preserves the aspect
    ratio.
    """
    if request.method == 'POST':
        url, height, width = request.form['url'], int(request.form['height']), int(request.form['width'])
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        new_size = (width, height)
        img.thumbnail(new_size)

        return serve_pil_image(img)

def serve_pil_image(pil_img):
    """
    Creates and returns a JPEG image from a Python Pillow Image Object.
    https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser
    """
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route("/report-generator", methods=['GET', 'POST'])
def report_generator():
    """
    """
    if request.method == 'POST':
        reports = request.form['reports']


    if request.method == 'GET':
        headings = ("Name", "Role", "Salary")
        data = (
            ("Jon", "Janitor", "30,000"),
            ("Bill", "Cook", "40,000"),
            ("Fred", "Pilot", "50,000")
        )
        return render_template('table.html', headings=headings, data=data)


@app.route("/", methods=['GET'])
def hello():
    return "Hello world!"