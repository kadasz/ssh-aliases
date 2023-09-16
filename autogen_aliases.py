#!/bin/env python3
import requests

# require settings
foreman_url = "https://foreman.domain.com/api/v2/hosts?per_page=9999"
username = "admin" 
password = "pass123"
headers = {
  "Content-Type": "application/json",
  "Accept": "application/json", 
{
