from django.shortcuts import render
from django.contrib import messages
import requests

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
        print(f"City received: {city}")

    else:
        city = 'kathmandu'

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8ae360e3150cb6ed95ef4e3dae28d393"
    param ={'units':'metric'}
    data= requests.get(URL,param).json()
    img_url=f"https://api.unsplash.com/search/photos?query={city}&per_page=1&client_id=DC9Bffb2vc9t_u81X9CKa6P7O7fGQrtzRYTDZnxC3Fk"
    img_data=requests.get(img_url).json()
    
    try:
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        speed=data['wind']['speed']
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        visibility=data['visibility']
        min_temp=data['main']['temp_min']
        max_temp=data['main']['temp_max']
        image=img_data['results'][0]['urls']['regular']
        return render(request, 'index.html', { 'city': city, 'temp': temp, 'icon': icon, 'desc': desc ,'speed': speed, 'humidity': humidity, 'pressure': pressure, 'visibility': visibility, 'min_temp': min_temp, 'max_temp': max_temp, 'image': image}) 
    except:
        temp=0
        desc='no city found'
        icon='01d'
        speed=0
        humidity=0
        pressure=0
        visibility=0
        min_temp=0
        max_temp=0
        image
        messages.error(request, 'City not found. Please try again.')
        return render(request, 'index.html', { 'city': city, 'temp': temp, 'icon': icon, 'desc': desc ,'speed': speed, 'humidity': humidity, 'pressure': pressure, 'visibility': visibility, 'min_temp': min_temp, 'max_temp': max_temp}) 
    







