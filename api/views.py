import os
import io
import re
import copy
import datetime

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from users.models import *

# Create your views here.

def index(request):
    context = {"title":"Duiqo", "login_page_url":"http://127.0.0.1:8000/app/home/"}
    return render(request, 'index_prev.html', context)

def application(request):
    return render(request, 'index.html')

def serve_app(request, exception):
    return render(request, 'index.html')


