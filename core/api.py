from core.models import Vacancy, Company, Interview
from core import serializers
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from datetime import datetime

# ----------------- SUPPORT FUNCTIONS -------------------------------------------------------------------------------
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 30


class VacancyViewset(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = [
        'actual_company__name',
        'recruitment_company__name',
    ]

    queryset = Vacancy.objects.all()

    def get_serializer_class(self):
        return serializers.VacancySerializer
    
class CompanyViewset(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    search_fields = [
        'name',
    ]

    queryset = Company.objects.all()

    def get_serializer_class(self):
        return serializers.CompanySerializer
    

class LatestInterview(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    now = datetime.now()

    queryset = Interview.objects.filter(datetime__lt=now).order_by('-datetime')[:1]

    def get_serializer_class(self):
        return serializers.InterviewSerializer
    

class UpcommingInterview(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    now = datetime.now()

    queryset = Interview.objects.filter(datetime__gt=now).order_by('datetime')

    def get_serializer_class(self):
        return serializers.InterviewSerializer