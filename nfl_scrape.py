from requests import get

from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import matplotlib as mlp
import matplotlib.pyplot as plt

url = 'https://www.reddit.com/r/wallstreetbets/comments/la0n4z/daily_discussion_thread_for_february_01_2021/'
response= get(url)

print(response.status_code)
print(response.content)

nfl = BeautifulSoup(response.content,'html.parser')
print(nfl.prettify())