from django.shortcuts import render
from stravalib.client import Client
from django.contrib.auth.models import User
import datetime

CLIENT_ID = "17148"
CLIENT_SECRET = "1b8bb7c47cb68b5ff0f03ca4c310a2c3262d828d"
REDIRECT_URI = "http://localhost:8000/strava_redirect"
accesToken = ''

def strava_auth(request):
    return render(request, 'strava_auth.html', {'auth_url': make_authorization_url()})

def strava_redirect(request):
    auth_code = request.GET.get("code")
    client = Client()
    access_token = client.exchange_code_for_token(CLIENT_ID, CLIENT_SECRET, auth_code)
    client.access_token = access_token
    
    global accesToken
    accesToken = access_token
    
    athlete = client.get_athlete()
    
    currentUser = User.objects.get(pk=request.user.id)
    currentUser.profile.stravaAccessToken = access_token
    currentUser.profile.save()
    
    return render(request, 'strava_redirect.html', {'athlete_name': athlete.username})


def strava_last_activity(request):
    currentUser = User.objects.get(pk=request.user.id)

    client = Client()
    client.access_token = currentUser.profile.stravaAccessCode
    
    activities = client.get_activities(before = datetime.datetime.now(), limit = 1)
    activityName = ''
    for activity in activities:
        activityName = activity.name
        downloadedActivity = client.get_activity(activity.id)
        activityStream = client.get_activity_streams(activity.id, types=["time", "watts"])
        averageCadence = downloadedActivity.average_cadence

    return render(request, 'strava_last_activity.html', {'activity_name' : averageCadence})


def make_authorization_url():
    client = Client()
    authorize_url = client.authorization_url(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope='view_private,write')
    print(authorize_url)
    return authorize_url


# Create your views here.
