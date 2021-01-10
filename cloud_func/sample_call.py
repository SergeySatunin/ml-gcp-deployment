import requests

# url of a deployed function
url = "https://us-central1-hale-treat-300918.cloudfunctions.net/test_gcf/pred"

params = {'G1':'1', 'G2':'0', 'G3':'0', 'G4':'0', 'G5':'0','G6':'0', 'G7':'0', 'G8':'0', 'G9':'0', 'G10':'0'}
result = requests.post(url, json = params)
print(result.json())