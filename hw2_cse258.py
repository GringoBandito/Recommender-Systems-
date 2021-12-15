import gzip
import math
import random
from collections import defaultdict
import numpy as np



pathway = "C:/Users/brand/Desktop/goodreads_reviews_comics_graphic.json.gz"


def parseData(fname):
    for l in gzip.open(fname):
        d = eval(l)
        yield d


data = list(parseData(pathway))

usersPerItem = defaultdict(set)
itemsPerUser = defaultdict(set)
ratingDict = {}

for d in data:
    user, item = d['user_id'], d['book_id']
    usersPerItem[item].add(user)
    itemsPerUser[user].add(item)
    ratingDict[(user,item)] = d['rating']
    
    
