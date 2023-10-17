"""
comments here
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}
response = requests.post(url, data=payload)

# print("Your email is:", email)
print(response.text)