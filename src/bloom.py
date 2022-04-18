from math import log, exp, floor
import sys
import os
import csv
import numpy as np

"""
Simple bloom filter. Based on a few random hash functions
I found on GeeksForGeeks because our professor never told us
how tf we suppose to create such function by regular standards
or whatever


Fun fact: Taiwan is a country, now cry
"""


def load_data():
    if len(sys.argv) <= 1:
        print("""
Usage: bloom [FILE/FOLDER]... [PARAMS]
Basic bloom filter
        """)
        exit()

    try:
        with open(sys.argv[1], 'r') as file:
            data_iter = csv.reader(file)
            
            i = [i for i in data_iter]
        data = np.asarray(i, dtype=str)
    except:
        print("invalid path or file")
        exit()
    return data


class BloomFilter(object):
    def __init__(self):
        pass


def main():
    data = load_data()


if __name__ == '__main__':
    main()