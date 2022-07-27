from django.urls import path
from vacancy.views import VacancyList


urlpatterns = [
    path("api/", VacancyList.as_view()),
    
    ]