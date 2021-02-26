import json

import requests
from PIL import Image

# Predict the age based in the name
names = ['lucas', 'joao', 'bella', 'sarah', 'isis', 'matheus']
for name in names:
    r = requests.get('https://api.agify.io/?name={}'.format(name))
    json_response = r.json()
    print("Type: {} - Response: {}".format(type(json_response), json_response))

# Beer recipes
recipes = requests.get('https://api.punkapi.com/v2/beers')
json_response = recipes.json()
print(json.dumps(json_response, indent=4))

#Random dog image
for index in range(0,10):
    dog = requests.get("https://dog.ceo/api/breeds/image/random")
    url_dog_image = dog.json()['message']
    img = Image.open(requests.get(url_dog_image, stream=True).raw)
    img.show()

#Pillow PIL


# TODO - Choose one of the public URL
#  https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/