from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer


class employeeList(APIView):
    def get(self, request):
        emp =  employee.objects.all()
        seri = employeeSerializer(emp, many = True)
        return Response(seri.data)
