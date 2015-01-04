# -*- coding: utf-8 -*-
import pandas as pd
import json
import sys
import os
import urllib
import json
import datetime
import searcher
from bs4 import BeautifulSoup

# Create your views here.

def get_images(keyword):
	print keyword
	keyword = keyword.encode('utf-8')
	images_naver = searcher.get_naver(keyword, 'image')
	images_daum = searcher.get_daum(keyword, 'image')

	return images_naver + images_daum
	

def main():
	save_path = "/home/ubuntu/web/socialpick"

	items = searcher.get_socialpick()

	item_dataframe = pd.DataFrame(items)
	item_dataframe['image_url'] = item_dataframe['keyword'].map(lambda x: get_images(x))
	item_dataframe.to_pickle(os.path.join(save_path, 'data', 'socialpick', searcher.get_today()))

if __name__=="__main__":
	main()
