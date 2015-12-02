#!/usr/bin/python
import sys
import csv
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if line[0].isdigit() and line[5] == 'question':
            tags = line[2].split()
            for tag in tags:
                print "{0}\t{1}".format(tag, 1)

if __name__ == '__main__':
    mapper()