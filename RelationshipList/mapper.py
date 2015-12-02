#! /usr/bin/python
import sys
import csv
def mapper():
    # using heap to store top k
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if line[0].isdigit():
            if line[5] == 'question':
                print "{0}\t{1}".format(line[0], line[3])
            elif line[5] == 'answer':
                print "{0}\t{1}".format(line[6], line[3])
            else:
                # print "comment?"
                pass
if __name__ == "__main__":
    mapper()