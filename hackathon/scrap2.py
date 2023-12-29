
# import matplotlib.pyplot as plt
import sqlite3
import requests
# from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.cur = self.db.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return [i[0] for i in self.cur.description], self.cur.fetchall()
headers = {"Accept-Language": "en-US, en;q=0.5"}
url="https://graduateway.com/psycoanalysis-essay/"
results = requests.get(url, headers=headers)
movie_soup = BeautifulSoup(results.text, "html.parser")
movie_div = movie_soup.find_all('article',class_='sample__body text-section__content')
fl=open("jeel.txt",'w')
for container in movie_div:
    for para in container.find_all('p'):
        print(para.text)
        fl.write(para.text+'\n')
fl.close()
        