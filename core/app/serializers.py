from rest_framework import serializers
from .models import Manager, Apartment, Client, ObjectName


class ApartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ManagerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('full_name', 'phone_number', 'email', 'created_date', 'number_of_deals')


class ManagerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class ManagerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('full_name', 'phone_number', 'email', )


