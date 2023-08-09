from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="headlines"),
    path('topnews', views.top, name='topnews'),
    path('trendingnews', views.trending, name='trendingnews'),
    path('sciencenews', views.science, name='sciencenews'),
    path('entertainment', views.entertainment, name='enternews'),
    path('sportsnews', views.sports, name='sportsnews'),
]