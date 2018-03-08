from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Suggestion_Model
from .forms import Suggestion_Form

from django.views.decorators.csrf import csrf_exempt

import json
import sys


# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html')

def suggestion_view(request):
    if request.method == 'POST':
        form = Suggestion_Form(request.POST)
        if form.is_valid():
            suggest = Suggestion_Model(
                suggestion=form.cleaned_data['suggestion']
            )
            suggest.save()
            form = Suggestion_Form()
    else:
        form = Suggestion_Form()
    suggestion_list = Suggestion_Model.objects.all()
    context={
        "suggestion_list":suggestion_list,
        "form":form
        }
    return render(request, 'suggestion.html',context)

@csrf_exempt
def suggestion_api(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            #print(json_data['data'])
            suggest = Suggestion_Model(suggestion=json_data['suggestion'])
            suggest.save()
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "PUT":
        json_data = json.loads(request.body)
        try:
            suggest = Suggestion_Model.objects.get(pk=json_data['id'])
            suggest.suggestion = json_data['suggestion']
            suggest.save()
            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == "DELETE":
        json_data = json.loads(request.body)
        try:
            suggest = Suggestion_Model.objects.get(pk=json_data['id'])
            suggest.delete()
            #print(json_data['data'])
            return HttpResponse("hello")
        except:
            return HttpResponse("Unexpected error:"+str(sys.exc_info()[0]))
    if request.method == 'GET':
        suggestion_list = Suggestion_Model.objects.all()
        suggestion_dictionary = {}
        suggestion_dictionary["suggestions"]=[]
        for suggest in suggestion_list:
            suggestion_dictionary["suggestions"] += [{
                "id":suggest.id,
                "suggestion":suggest.suggestion
            }]
        print(suggestion_dictionary)
        return JsonResponse(suggestion_dictionary)

def page(request, page_num):
    if page_num>=1:
        example_list=[]
        for i in range(page_num):
            example_list+=[i+1]

    else:
        example_list=None
    #return HttpResponse("Hello World")
    context={
        "page_template":page_num,
        "example_list":example_list
        }
    return render(request, 'page.html',context)
