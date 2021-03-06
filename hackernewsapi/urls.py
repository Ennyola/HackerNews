"""hackernewsapi URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from news.views import list_news, type_job, news_details, ask_hn, show_hn
urlpatterns = [
    path('', list_news, name="index"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('ask/', ask_hn, name="ask"),
    path('item/<int:id>/', news_details, name="details"),
    path('job/', type_job, name="job"),
    path('show/', show_hn, name="show"),


]
