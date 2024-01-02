from flask import Flask, g, request, redirect, url_for
from flask import render_template

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

app = Flask(__name__)

CLIENT_ID = config.SPOTIPY_CLIENT_ID
CLIENT_SECRET = config.SPOTIPY_CLIENT_SECRET
REDIRECT_URI = config.REDIRECT_URI
scope = ['user-library-read', 'user-top-read']

def get_auth():
    if g.sp == None:
        g.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

@app.before_request
def before_request():
    g.sp = None

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/mode-select", methods=['GET', 'POST'])
def select_mode():
    if g.sp == None:
        get_auth()

    if request.method == 'POST':
        mode = request.form['mode']
        return redirect(url_for('select_options', mode=mode))
    
    else:
        return render_template("form1.html")

@app.route("/options/<mode>")
def select_options(mode):
    if g.sp == None:
        get_auth()

    if mode == "top-tracks":
        return "<p>top tracks mode</p>" # placeholder to get form flow working
    elif mode == "playlists":
        return "<p>playlists mode</p>" # placeholder to get form flow working
    elif mode == "saved-tracks":
        return "<p>saved tracks mode</p>" # placeholder to get form flow working
    else:
        return "<p>No mode selected</p>"
    

# @app.route("/select")
# def form():
#     if g.sp == None:
#         get_auth()

#     return render_template("index.html", sp=g.sp)
