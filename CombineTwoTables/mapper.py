#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    node_count = 0
    user_count = 0
    for line in reader:
          
        # YOUR CODE HERE
        if len(line) == 19:
            if line[0].isdigit():
                writer.writerow([line[3]] + ['B'] + line[0:3] + line[5:10])
        elif len(line) == 5:
            if line[0].isdigit():
                writer.writerow([line[0]] + ['A'] + line[1:])
if __name__ == '__main__':
    mapper()