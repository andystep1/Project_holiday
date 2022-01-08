from typing import Mapping
from fastapi import FastAPI
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = FastAPI()

@app.get('/get_recommendations')
async def get_recommendations(search):

    #Init
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

    #Search: return JSON of the first result
    result = sp.search(q = search, type = 'track', limit = 1)

    #Get ID of the track. Need a list for the recommendation lookup
    id_list = [result['tracks']['items'][0]['id']]

    return sp.recommendations(seed_tracks = id_list, limit = 10)

@app.get("/")
async def root():
    return {"message": "Hello World"}
