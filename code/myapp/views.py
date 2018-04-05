from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

import json
import sys


# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html')

@login_required(login_url='/login/')
def suggestion_view(request):
    if request.method == 'POST':
        form = Suggestion_Form(request.POST)
        if form.is_valid():
            suggest = Suggestion_Model(
                suggestion=form.cleaned_data['suggestion'],
                author=request.user
            )
            suggest.save()
            return redirect("/")
    else:
        form = Suggestion_Form()
    #comm_form=Comment_Form()
    # suggestion_list = Suggestion_Model.objects.all()
    context={
        # "suggestion_list":suggestion_list,
        "form":form,
        #"comm_form":comm_form
        }
    return render(request, 'suggestion.html',context)

@login_required(login_url='/login/')
def comment_view(request, suggest_id):
    if request.method == 'POST':
        comm_form = Comment_Form(request.POST)
        if comm_form.is_valid():
            comm_form.save(suggest_id,request.user)
            return redirect("/")
            #form = Suggestion_Form()
    else:
        comm_form = Comment_Form()
    #form = Suggestion_Form()
    # suggestion_list = Suggestion_Model.objects.all()
    context={
        # "suggestion_list":suggestion_list,
        #"form":form,
        "comm_form":comm_form,
        "suggest_id":suggest_id
        }
    return render(request, 'comment.html',context)


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
            comment_list = Comment_Model.objects.filter(suggestion=suggest)
            #print(comment_list)
            comment_json = []
            for comm in comment_list:
                comment_json+=[{
                    "comment":comm.comment,
                    "id":comm.id,
                    "author":comm.author.username,
                    "created_on":comm.created_on
                }]
            suggestion_dictionary["suggestions"] += [{
                "id":suggest.id,
                "comments":comment_json,
                "suggestion":suggest.suggestion,
                "created_on":suggest.created_on,
                "author":suggest.author.username
            }]
        # print(suggestion_dictionary)
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

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    else:
        form = registration_form()
    context = {"form":form}
    return render(request,"registration/register.html",context)
