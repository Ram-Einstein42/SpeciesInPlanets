import json
from urllib.request import urlopen

planet_url = 'https://swapi.dev/api/planets/'


def api_call(url: str) -> dict:
    json_url = urlopen(url)
    return json.loads(json_url.read())    # converts json to dict