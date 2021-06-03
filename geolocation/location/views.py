from django.shortcuts import render
import requests
import json
import socket
# Create your views here.
def index(request):
    url1 = 'http://ip-api.com/json/'
    res1 =requests.get(url1)
    load= json.loads( res1.text )
    ip = load['query']
    print(str(ip))
    #ip = url1['query']
    url = 'http://ip-api.com/json/'+ip+'?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,query'
    res = requests.get(url)
    print(res.text)
    loc_info = json.loads(res.text)
    print(loc_info)
    #location_data = res.text
    if loc_info['status'] == 'success':
        context = {'data' : loc_info}
    elif loc_info['status'] == 'fail' or loc_info['message']=='invalid query':
        context = {'data':''}
        print(context)
    return render(request , 'index.html',context)

def home(request):
    try:
        if request.POST:
            ip = request.POST.get("ip")
            url = 'http://ip-api.com/json/'+ip+'?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,query'
            res = requests.get(url)
            print(res.text)
            loc_info = json.loads(res.text)
            print(loc_info)    
            if loc_info['status'] == 'success':
                context = {'data' : loc_info}
                return render(request,'index.html',context)
            elif loc_info['status'] == 'fail' or loc_info['message']=='invalid query':
                context = {'data':''}
                return render(request,'index.html',context)
        
    except:
        context = {'data':''}
        return render(request,'index.html',context)
        
    return render(request,'home.html')