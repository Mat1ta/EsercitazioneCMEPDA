import os
import argparse
import logging
import time
import string
#import matplotlip.pyplot as plt

parser = argparse.ArgumentParser(description='measure the relative frequency of the letters of the alphabet in a text')
parser.add_argument('testo', help='prende come stringa il nome del file da analizzare')
parser.add_argument('-isto', '--istogramma', help='print the histogram of the frequences', action='store_true')
args= parser.parse_args()

def from_txt_to_str(txt=None):
    file = open(txt,'r')
    file.seek(0)
    file.close
    return file.read()

test=from_txt_to_str(args.testo)
dic = { key : 0 for key in string.ascii_lowercase }

