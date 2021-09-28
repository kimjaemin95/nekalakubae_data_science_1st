from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
soup = bs4(response.text, "html.parser")

soup.find_all


