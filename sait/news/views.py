from django.shortcuts import render
from menu.models import Menu
import requests


def news(request):
    menus = Menu.objects.all().order_by('order')
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-09-22&sortBy=publishedAt&apiKey=1dc50907bfcd45cba46078deb6b21e4d'

    response = requests.get(url)
    print(response)
    data = response.json()

    articles = data['articles']
    desc = []
    news = []
    img = []

    for article in articles:
        if article['description'] != '[Removed]':
            news.append(article['title'])
            desc.append(article['description'])
            img.append(article['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'news.html', context={"mylist": mylist, 'menus': menus})
