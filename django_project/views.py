import requests
from django.shortcuts import render

def home(request):
    # Using APIs
    response = requests.get("https://api.github.com/events")
    data = response.json()
    result = data[0]['repo']

    # Example 2
    response2 = requests.get("https://catfact.ninja/fact")
    data2 = response2.json()
    result2 = data2['fact']

    return render(request, 'templates/index.html', {'result': result, 'result2': result2})