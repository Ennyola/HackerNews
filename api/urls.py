from django.urls import path,include
from .views import News,singleNews
urlpatterns = [
    path('news/', include([
        path('',News.as_view()),
        path('<int:id>/',singleNews.as_view())
    ]))       
]
