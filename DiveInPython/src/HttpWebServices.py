'''
Created on Mar 29, 2017

@author: griz
'''

from stravalib.client import Client
from flask import Flask
from flask import request
import httplib2
import time

CLIENT_ID = "17148"
CLIENT_SECRET = "1b8bb7c47cb68b5ff0f03ca4c310a2c3262d828d"
REDIRECT_URI = "http://localhost:65010/strava_callback"
AUTORIZATION_CODE = "3891aee1a5dcf2a9dc3e5329cbf6bba3bcdc65c0"

access_token = '509dd667c019b1d799e923abfeec2dcae431136f'

def start_web_server():
    app = Flask(__name__)
    client = Client()
    @app.route('/')
    def homepage():
        text = '<a href="%s">Authenticate with strava</a>'
        return text % make_authorization_url()
    
    @app.route('/strava_callback')
    def strava_callback():
        global access_token
        print('Authorization code is:')
        print(request.args.get('code'))
        text = '<p>Received the token</p>'
        # Extract the code from your webapp response
        code = request.args.get('code') # or whatever your framework does
        access_token = client.exchange_code_for_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, code=code)
    
        # Now store that access token somewhere (a database?)
        client.access_token = access_token
        athlete = client.get_athlete()
        print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))
        fileToUpload = open('/home/griz/garmin/activities/2017-04-05_20-00-12-80-45144.fit', 'rb')
        activityUploader = client.upload_activity(fileToUpload, 'fit', 'TestActivity', '', 'ride', False, '1')

        return text

    def make_authorization_url():
        authorize_url = client.authorization_url(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope='view_private,write')
        print(authorize_url)
        return authorize_url

    app.run(debug=True, port=65010)


if __name__ == '__main__':
    '''print('Running some webservices examples')
    httplib2.debuglevel = 1
    h = httplib2.Http('.cache')
    response, content = h.request('http://www.diaconescuradu.com/contraatacul-babelor-alergare-si-bicicleta-intr-un-weekend-ploios')
    print(response.status)
    print(len(content))
    print(response.fromcache)
    response1, content1 = h.request('http://www.diaconescuradu.com/contraatacul-babelor-alergare-si-bicicleta-intr-un-weekend-ploios', headers={'cache-control':'no-cache'})
    print('\n')
    print(response1)
    '''
    #client = Client()
    #authorize_url = client.authorization_url(client_id=1234, redirect_uri='http://localhost:65010/authorized')
    #print(authorize_url)
    # Have the user click the authorization URL, a 'code' param will be added to the redirect_uri
    # .....

    # Extract the code from your webapp response
    #code = request.get('code') # or whatever your framework does
    #access_token = client.exchange_code_for_token(client_id=1234, client_secret='asdf1234', code=code)

    # Now store that access token somewhere (a database?)
    #client.access_token = access_token
    #athlete = client.get_athlete()
    #print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))
    
    
    #Needed for getting new access token
    #start_web_server()
    
    client = Client()
    client.access_token = access_token
    athlete = client.get_athlete()
    print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))
    fileToUpload = open('/home/griz/garmin/activities/2017-04-05_20-00-12-80-45144.fit', 'rb')
    activityUploader = client.upload_activity(fileToUpload, 'fit', 'Ultima tura', '', 'ride', False, '1')
    while not activityUploader.is_complete or activityUploader.is_processing:
        activityUploader.poll()
        time.sleep(1)
    #print(activityUploader.is_error)
    pass