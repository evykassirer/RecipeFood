from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import requests
import json

def index(request):
	"""rstr = "http://api.yummly.com/v1/api/recipes?_app_id=8397ddf3&_app_key=5ddd5532a314c79efcb9e7cede1b98a5"
	rstr += "&allowedIngredient[]=bread&allowedIngredient[]=yogurt"
	rstr += "&allowedIngredient[]=bread&allowedIngredient[]=bread"
	r = requests.get(rstr)
	yummly = r.json()
	return HttpResponse(yummly["attribution"]["html"])"""
	template = loader.get_template('recipe/index.html')
	context = RequestContext(request, {  
	})
	return HttpResponse(template.render(context))

def showrecipe(request):
	if request.method != 'POST':
		return HttpResponse("Method didn't equal post")
	rstr = "http://api.yummly.com/v1/api/recipes?_app_id=8397ddf3&_app_key=5ddd5532a314c79efcb9e7cede1b98a5"
	for key in request.POST :
		rstr += "&allowedIngredient[]="
		rstr += request.POST[key]
	r = requests.get(rstr)
	yummly = r.json()
	return HttpResponse(yummly["attribution"]["html"])