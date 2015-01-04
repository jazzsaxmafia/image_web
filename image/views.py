# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import pandas as pd
import json
import sys 
import os
import urllib
import searcher 
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
	return render_to_response('home.html')

def image(request):
	return render_to_response('image.html')

def get_query(request):
	
	query = request.GET.get('query').encode('utf-8')
	
	items_naver = searcher.get_naver(query, 'image')
	items_daum = searcher.get_daum(query, 'image')
	
	all_items = items_naver + items_daum
	return render_to_response('image.html', {'naver':items_naver, 'daum':items_daum})

def socialpick_image_structure(row):
	current_item = json.dumps({'keyword': row['keyword'], 'images': row['image_url']})
	print current_item
	return current_item

def socialpick(request):
	socialpick_path = "/home/ubuntu/web/socialpick"
	today = searcher.get_today()

	pickle_file = os.path.join(socialpick_path, 'data', 'socialpick', today)

	socialpick_dataframe = pd.read_pickle(pickle_file)

	all_items = []
	all_items = socialpick_dataframe.apply(lambda x: socialpick_image_structure(x), 1)
	all_items = all_items.map(lambda x: json.loads(x))
	return render_to_response('socialpick.html', {'data':all_items})
