"""Covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from covidtracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('india/',views.india,name="india"),
    path('indian_state/<str:state>/',views.indian_state,name="indian_state"),
    path('country/<str:country>/',views.country,name="country"),

    path('covid_news/',views.covidnews,name="covidnews"),
    path('news/',views.news,name="news"),

    path('mynews/',views.mynews,name="mynews"),

    path('monkey/',views.monkeypox,name="monkeypox"),
]
