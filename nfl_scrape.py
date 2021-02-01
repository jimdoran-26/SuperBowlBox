from requests import get

from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import matplotlib as mlp
import matplotlib.pyplot as plt

url = 'https://www.google.com/search?client=safari&sxsrf=ALeKk01BTAXAQUs-YfDE9MQ6ww3k8mSSGg%3A1612134496567&source=hp&ei=YDgXYPSVH-Wmgge18LHIBA&q=bucs+cheifs&oq=bucs+cheifs&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIHCAAQsQMQCjIECAAQCjIECAAQCjoHCCMQ6gIQJzoOCC4QsQMQxwEQowIQkwI6CwguELEDEMcBEKMCOggILhDHARCjAjoICAAQsQMQgwE6CAguELEDEIMBOgQIIxAnOgUIABCRAjoECAAQQzoHCC4QsQMQQzoECC4QQzoFCAAQsQM6CggAELEDEIMBEEM6BwgAELEDEEM6BwgAEBQQhwI6BAgAEAM6AggAOg0IABCxAxCDARAUEIcCUNGaGVjWpxlgjakZaAFwAHgAgAG4AYgBlwmSAQM3LjSYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwj0xfr_pMfuAhVlk-AKHTV4DEkQ4dUDCAw&uact=5#sie=m;/g/11byxflc60;6;/m/059yj;dt;fp;1;;'
response= get(url)

print(response.status_code)
print(response.content)

nfl = BeautifulSoup(response.content,'html.parser')
print(nfl.prettify())