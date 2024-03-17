import requests
from django.core.cache import cache
from django.shortcuts import render


def get_data():
    url = 'https://raw.githubusercontent.com/sibylassana95/Listes-des-plantes/main/plante.json'
    data = cache.get(url)
    if not data:
        response = requests.get(url)
        data = response.json()
        cache.set(url, data)
    return data


def index(request):
    plantes = get_data()
    query = request.GET.get('q')
    if query:
        plantes = [plante for plante in plantes if query.lower()
                   in plante['name'].lower()]
    context = {'plantes': plantes, 'query': query}
    return render(request, 'index.html', context)
