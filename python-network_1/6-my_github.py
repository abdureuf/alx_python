"""
any comments 
"""
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, password))
data = response.json()

if response.status_code == 200:
    print(data['id'])
else:
    print("None")