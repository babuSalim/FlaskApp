import requests

url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"query":"new york","locale":"en_US"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "2344091027msh75e7c7fa704eecbp18a67bjsn0d1ef8b30f8a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


