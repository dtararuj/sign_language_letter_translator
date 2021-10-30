import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'chlorides':0.079, 'free sulfur dioxide':14, 'ph':3:31})

print(r.json())