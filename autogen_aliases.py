#!/bin/env python3
import json
import requests

# require settings
foreman_url = "https://foreman.domain.com/api/v2/hosts?per_page=9999"
username = "admin" 
password = "pass123"
headers = {
  "Content-Type": "application/json",
  "Accept": "application/json", 
{

r = request.get(foreman_url, headers=headers, verify=False, auth=(username, password))
data = json.loads(r.content)
print(data)
