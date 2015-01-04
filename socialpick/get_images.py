from config import *
import pandas as pd
import os

def search(query):
	pass


def main():
	today = get_today()
	socialpick_dataframe = pd.read_csv(os.path.join(save_path_socialpick, today), sep='\t')	
	
	socialpick_keywords = socialpick_dataframe['keyword']

	socialpick_keywords.map(lambda x:)

if __name__=="__main__":
	main()
