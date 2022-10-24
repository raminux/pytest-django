from rest_framework import serializers
from companies import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ['id', 'name', 'status', 'application_link', 'last_update', 'notes']
        