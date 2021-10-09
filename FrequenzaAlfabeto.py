import os
import argparse
import logging
import time
import string
#import matplotlip.pyplot as plt

parser = argparse.ArgumentParser(description='measure the relative frequency of the letters of the alphabet in a text')
<<<<<<< HEAD
parser.add_argument('testo', help='insert the file .txt that you want to be analysed')
parser.add_argument('-isto', '--istogramma', help='print the histogram of the frequences", action="store_true')
=======
parser.add_argument('testo', help='prende come stringa il nome del file da analizzare')
parser.add_argument('-isto', '--istogramma', help='print the histogram of the frequences', action='store_true')
>>>>>>> ad0a09cda401d3f85a030eaaefc2aa2eb4e5e607
args= parser.parse_args()

def from_txt_to_str(txt=None):
    file = open(txt,'r')
    file.seek(0)
    file.close
    return file.read()

test=from_txt_to_str(args.testo)
dic = { key : 0 for key in string.ascii_lowercase }

def print_dictonary (txt = None , dict = None):
    
 for val in txt:
    if val.isalpha():
        dict[val]=dict[val]+1
    i=i+1
    
  print(dict)
  
def histogram (dict = None):
    if args.istogramma:
        plt.bar(list(dic.keys()), dic.values(), color='b')
        plt.show()
        
        

