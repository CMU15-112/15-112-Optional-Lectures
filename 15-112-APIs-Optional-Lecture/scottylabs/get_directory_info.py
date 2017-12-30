import requests
import json
import pprint

# Setup parameters
andrew_id = "fmarsh"

# Send request
url = "http://apis.scottylabs.org/directory/v1/andrewID/" + andrew_id
response = requests.get(url)
if (response.status_code == 200):
    data = response.json()
else:
    print("Failed: ", response)
    exit(0)

# Print out the results in a nice format
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
