from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import Flask, request, jsonify
import json

DEFAULT_TAG = "python_sample_basic"
application = Flask(__name__)

@application.route('/cloudinary', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.data
        dataDict = json.loads(data)
        # print(dataDict['url'])
        response = upload_files(dataDict['url'], dataDict['name'])
        return jsonify({ 'url': response['url'], 'height': response['height'], 'width': response['width'] })
    else:
        return 'GET'

def upload_files(url, name='test'): 
    print("--- Upload by fetching a remote image")
    response = upload(
        url,
        public_id=name,
        tags=DEFAULT_TAG
    )
    return response

# for troubleshooting 
def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))
         
