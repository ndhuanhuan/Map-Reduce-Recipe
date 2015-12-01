#!/usr/bin/python
import sys
import csv
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if line[0].isdigit():
            if line[6].isdigit(): 
                #this is answer,output format is parent_id, post_id, and answer length
                print "{0}\t{1}\t{2}".format(line[6], line[0], len(line[4]))
            else: 
                #this is question, output format is post_id, and length of post
                print "{0}\t{1}".format(line[0], len(line[4]))
if __name__ == '__main__':
    mapper()