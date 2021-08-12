from django.shortcuts import render
import requests
import json
import time

# Create your views here.
def data(request):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    context = {}

    if request.method == 'POST':
        city = request.POST['cityname']

        querystring = {"q":city, "units":"\"imperial\""}

        headers = {
            'x-rapidapi-key': "b49a212520msh7b1e3f346f09330p152f8ejsn027c6df363f6",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        try:
            context = {
                'description' : response['weather'][0]['description'],
                'icon' :  'https://openweathermap.org/img/wn/' + response['weather'][0]['icon'] + '@2x.png',
                'temperature' : round(response['main']['temp']-273.15, 2),
                'city' : response['name'],
                'country' : response['sys']['country'],
                'time' : time.strftime('%H:%M', time.localtime(response['dt']+response['timezone'])),
                'date' : time.strftime('%d/%m', time.localtime(response['dt']+response['timezone']))
            }
        except:
            context = {'city': 0}
    
    return render(request, 'main.html', context)
