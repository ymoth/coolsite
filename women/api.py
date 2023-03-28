"""
Creating a 22.03.2023 11:00 code in a file `api`
Description: 
"""
import rest_framework.response
from django.contrib.auth.models import User
from django.http import HttpRequest
from rest_framework import views, viewsets
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from women.models import Women


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=10)
    content = serializers.CharField()


class WomenAPI(ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class UserSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    username = serializers.CharField()
    last_login = serializers.DateTimeField()


class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    