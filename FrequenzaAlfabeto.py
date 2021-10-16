import os
import argparse
import logging
import time
import string
import matplotlip.pyplot as plt
import unittest

parser = argparse.ArgumentParser(description='measure the relative frequency of the letters of the alphabet in a text')
parser.add_argument('testo', help='insert the file .txt that you want to be analysed')
parser.add_argument('-isto', '--istogramma', help='print the histogram of the frequences', action='store_true')
args= parser.parse_args()

def from_txt_to_str(txt=None):
    """it opens and read the file, it returns a string with all the contents of the given file
    """
    file = open(txt,'r')
    file.seek(0)
    file.close
    return file.read()

def dictionary (txt = None , dict = None):
    """it counts the frequency of each letter, and save all in the given dictionary
    """
    Testo=txt.lower()
    for val in Testo:
        if val.isalpha():
            dict[val]=dict[val]+1
        return dict

def histogram (dict = None):
    """it plots and show the histogram of the frequencies that are saved in the given dictionary
    """
    plt.bar(list(dic.keys()), dic.values(), color='b')
    plt.show()



dic = { key : 0 for key in string.ascii_lowercase}
test=from_txt_to_str(args.testo)
dic=dictionary(txt=test, dict=dic)
if args.istogramma: histogram(dic)
