#!/usr/bin/python

import csv
import sys
import re
from string import maketrans
def mapper():
    #word frequency
    count = 0
    pattern = re.compile('[\n \.,!\?:;"\(\)<>\[\]#\$=\-/]')
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        line_split = pattern.split(line[4])
        for word in line_split:
            if word == 'fantastic':
                count += 1
    print count

def mapper2():
    #inverted index
    node_id = []
    pattern = re.compile('[\n \.,!\?:;"\(\)<>\[\]#\$=\-/]')
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        line_split = pattern.split(line[4])
        for word in line_split:
            if word.lower() == 'fantastically':
                node_id.append(line[0])
                continue
    print node_id

if __name__ == '__main__':
    mapper2()