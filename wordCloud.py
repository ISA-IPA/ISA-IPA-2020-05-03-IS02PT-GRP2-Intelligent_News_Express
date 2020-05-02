from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import io
import sqlite3
from sqlite3 import Error
import util

def run():
	conn = util.create_connection("./db/news.db")
	summaries = util.getAllSummary(conn)
	text = ""
	for row in summaries:
	    for item in row:
	        item = item.encode("utf-8")
	        text = text + item + " "

	wc = WordCloud(background_color="white")
	wc.generate(text)
	wc.to_file('cloud_word_summary_1.png')
	custom_mask = np.array(Image.open("cloud.png"))
	wc = WordCloud(background_color="white", mask=custom_mask, contour_width=3, contour_color='white')

	wc.generate(text)
	wc.to_file('cloud_word_summary_2.png')
	print("Image generated")