from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import pandas as pd
import json
import sys 
import os
import urllib
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
	return render_to_response('home.html')

def get_query(request):
	query = request.GET.get('query')
	key = '5d8f3e56c2afa7ad444d6b53feed0179' 
	params = ['key', 'query', 'target', 'start', 'display']
	params_val = [key, query, 'image', '1', '100']

	url = 'http://openapi.naver.com/search?'
	for i in range(len(params)):
		url += params[i] + '=' + params_val[i] + '&'
		
	data = urllib.urlopen(url[:-1]).read()

	soup = BeautifulSoup(data)
	items = soup.find_all('item')
	
	all_items = []

	for item in items:
		title = item.title.getText
		link = item.link.getText
		image = item.thumbnail.getText

		print >> sys.stderr, image
		
		current_item = {'title':item.title, 'link':link, 'image':image}
		all_items.append(current_item)
	
	return render_to_response('home.html', {'data':all_items})
#	return HttpResponse(json.dumps({'data':all_items}))

	
	
