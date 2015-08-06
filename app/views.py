from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.db import connection
from models import NewsFeeds
import json
from django.core import serializers

# Create your views here.


def home(request):
    all_entries =  NewsFeeds.objects.all()
    data = serializers.serialize('json',list(all_entries))
    return HttpResponse(data, content_type="json")

def index(request):

    return render_to_response('index.html')
