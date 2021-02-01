from django.shortcuts import render
from .models import Person
from rest_framework import viewsets, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PersonSerializer
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PersonView(viewsets.ModelViewSet):
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'email')
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

def home_page(request) :
    return HttpResponse('You are in Home Page. Go to /apis')
