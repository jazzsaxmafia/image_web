# -*- coding: utf-8 -*-
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

def news(request):
	return render_to_response('news.html')

def get_query(request):
	
	query = request.GET.get('query').encode('utf-8')
	
	items_naver = get_naver(query)
	#items_daum = get_daum(query)
	
	all_items = items_naver# + items_daum
	return render_to_response('news.html', {'data':items_naver})#, 'daum':items_daum})

	
def get_naver(query):
	key = '5d8f3e56c2afa7ad444d6b53feed0179' 
	base_url = 'http://openapi.naver.com/search'

	params = {'key':key, 'query':query, 'target':'news', 'start':1, 'display':100}
	url = base_url + '?' + urllib.urlencode(params)

	return get_items(url)

def get_daum(query):
	key = '237bc4b34763740433c5c5918703da1a1fb0e64f'	
	base_url = "http://apis.daum.net/search/news"

	all_items = []
	for i in range(1,6):
		params = {'q':query, 'apikey':key, 'result':20, 'pageno':i}
		url = base_url +'?' + urllib.urlencode(params)
		all_items += get_items(url)

	return all_items

def get_items(url):
	search_result = urllib.urlopen(url)
	data = search_result.read()
	soup = BeautifulSoup(data)
	
	items = soup.find_all('item')
	all_items = []
	for item in items:
		title = item.title.getText()
		link = item.originallink.getText()
		description = item.description.getText()
		current_item = {'title':title, 'link': link, 'description':description}
		all_items.append(current_item)
	
	return all_items

#	return soup.find_all('item')
