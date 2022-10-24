from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from companies import serializers
from companies import models


class CompanyViewSet(ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all().order_by('-last_update')
    pagination_class = PageNumberPagination
