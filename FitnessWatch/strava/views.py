from django.shortcuts import render
from stravalib.client import Client

CLIENT_ID = "17148"
CLIENT_SECRET = "1b8bb7c47cb68b5ff0f03ca4c310a2c3262d828d"
REDIRECT_URI = "http://localhost:8000/strava_redirect"

def strava_auth(request):
    return render(request, 'strava_auth.html', {'auth_url': make_authorization_url()})

def strava_redirect(request):
    auth_code = request.GET.get("code")
    client = Client()
    access_token = client.exchange_code_for_token(CLIENT_ID, CLIENT_SECRET, auth_code)
    client.access_token = access_token
    athlete = client.get_athlete()
    
    return render(request, 'strava_redirect.html', {'athlete_name': athlete.username})

def make_authorization_url():
    client = Client()
    authorize_url = client.authorization_url(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope='view_private,write')
    print(authorize_url)
    return authorize_url


# Create your views here.
