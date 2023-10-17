"""
only import requests
"""
import requests

response = requests.get("https://alu-intranet.hbtn.io/status")
data = response.text

print("Body response:")
print("\t- type:", type(data))
print("\t- content:", data.strip())