from django.shortcuts import render
import requests
import json
# Create your views here.
def Index(req):
    ip = requests.get('https://api64.ipify.org?format=json')
    ip_data =json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/24.48.0.1'+ip_data[ip])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    context = {'data':location_data}
    return render(req,'index.html',context)