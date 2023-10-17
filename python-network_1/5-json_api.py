"""
any comments 
"""
import requests
import sys

url = 'http://0.0.0.0:5000/search_user'
letter = sys.argv[1] if len(sys.argv) > 1 else ""

payload = {'q': letter}
response = requests.post(url, data=payload)

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")