from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json

from .models import Drug
from CLML.save_to_db import data_to_db
from .search_db import search_drug_from_db


# 将数据存入数据库
def save_data(request):
    data_to_db()
    return HttpResponse("Save data successfully!")


@require_http_methods(['GET'])
def search_drug(request):
    response = {}
    try:
        drug_name = request.GET.get('drug_name')
        n = int(request.GET.get('n', 10))
        known_results, predict_results = search_drug_from_db(drug_name)
        response['msg'] = 'success'
        response['error_num'] = 0
        response['known_results'] = known_results
        response['predict_results'] = predict_results    #[:n]
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
