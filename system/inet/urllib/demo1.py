import json
import urllib.request


URL = 'http://api.open-notify.org/astros.json'
astros_json_bin = urllib.request.urlopen(URL)
astros = json.load(astros_json_bin)
ASTROS = astros.get('people')
print('на орбите', astros.get('number'), 'космонавта:')
for astr in ASTROS:
    print(astr.get('name'))