"""
any comments 
"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)
request_id = response.headers.get('X-Request-Id')

print(request_id)