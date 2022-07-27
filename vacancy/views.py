from vacancy.models import Vacancy
from vacancy.serializers import VacancyDetailSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('vacancy_type',)