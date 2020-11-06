import requests
from pprint import pprint

r = requests.get('https://google.com')
texte=r.text
pprint(texte)

texte=r.content
pprint(texte)

