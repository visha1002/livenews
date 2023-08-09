from django.shortcuts import render
import requests

# Create your views here.
# https://inshortsapi.vercel.app/news?category=all
def index(request):
    records = {}
    url = requests.get("https://inshorts.me/news/all?offset=0&limit=21")
    inshorts_data = url.json()
    records['alldata'] = inshorts_data
    return render(request, 'index.html', records)

def top(request):
    records1 = {}
    url = requests.get("https://inshorts.me/news/top?offset=0&limit=21")
    top_data = url.json()
    records1['topdata'] = top_data
    return render(request, 'top.html', records1)

def trending(request):
    records2 = {}
    url = requests.get("https://inshorts.me/news/trending?offset=0&limit=21")
    trending_data = url.json()
    records2['topdata'] = trending_data
    return render(request, 'top.html', records2)

def science(request):
    records3 = {}
    url = requests.get("https://inshorts.me/news/topics/science")
    science_data = url.json()
    records3['sciencedata'] = science_data
    return render(request, 'science.html', records3)

def entertainment(request):
    records4 = {}
    url = requests.get("https://inshorts.me/news/topics/entertainment")
    enter_data = url.json()
    records4['enterdata'] = enter_data
    return render(request, 'entertainment.html', records4)

def sports(request):
    records5 = {}
    url = requests.get("https://inshorts.me/news/topics/sports")
    sports_data = url.json()
    records5['sportsdata'] = sports_data
    return render(request, 'sports.html', records5)