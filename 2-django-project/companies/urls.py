from rest_framework import routers
from companies import views

companies_router = routers.DefaultRouter()
companies_router.register('', viewset=views.CompanyViewSet, basename='companies')