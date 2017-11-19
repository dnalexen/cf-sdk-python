#------------------------------------------------------------------------------
# Dominant color palette. 
# POST /v1/colors/dominant_colors
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin
from pprint import pprint

from props import *

# Replace this with the custom url generated for you.
api_gateway_url = props['api_gateway_url']

# Pass the api key into the header
# Replace 'your_api_key' with your API key.
headers = {'X-Api-Key': props['X-Api-Key']}

params = {}

# Optional parameters.
params['color_count'] = 3
params['quality'] = 1
params['image_max_dimension'] = 256

api_endpoint = '/v1/colors/dominant_colors'

url = urljoin(api_gateway_url,api_endpoint)

headers['Content-Type'] = 'image/jpeg'

response = requests.post(url,
                         headers=headers,
                         params=params,
                         data=open('test_image_2.jpeg','rb'))

print response.status_code
pprint(response.json())
