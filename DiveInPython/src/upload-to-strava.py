#!/usr/bin/python
#
# Script to run the FIT-to-TCX converter on every new FIT file that is being
# downloaded by Garmin-Extractor.
#
# Adjust the fittotcx path to point to where you have put the FIT-to-TCX files.
#
# Copyright (c) 2012, Gustav Tiger <gustav@tiger.name>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import errno
import os
import subprocess
import sys
import shutil

from stravalib.client import Client
import time

access_token = '509dd667c019b1d799e923abfeec2dcae431136f'


def main(action, filename):
    if action == "DOWNLOAD":
        client = Client()
        client.access_token = access_token
        athlete = client.get_athlete()
        print("For {id}, I now have an access token {token}".format(id=athlete.id, token=access_token))
        fileToUpload = open(filename, 'rb')
        activityUploader = client.upload_activity(fileToUpload, 'fit', 'TestActivity', '', 'ride', False, '1')
        activityUploader.wait(60, 1)
        print('Finished uploading to strava')
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))

