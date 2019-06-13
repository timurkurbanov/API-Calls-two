import json
import requests

response = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
countries = json.loads(response.content)

print(countries[0].keys())
print(len(countries))

#Pick a country.
print(countries[5])

#Extract the URL for the JSON data about the government of the country of your choice (if the country has more than one governmental body - like how Canada has both the House of Commons and the Senate - you can just pick one of them).
goverment_url = countries[5]['legislatures'][0]['popolo_url']

#Make another request to get that government-specific JSON data.
response_two = requests.get(goverment_url)
countries_two = json.loads(response_two.content)
print(countries_two.keys())
print(len(countries_two['persons']))

#Extract the name of one politician from that JSON response and save it in a variable.
name = countries_two['persons'][0]['name']
print(name)