#!/usr/bin/python
import sys
import csv
from datetime import datetime
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if line[3].isdigit():
            time_part = line[8].split()
            hour = datetime.strptime(' '.join([time_part[0], time_part[1][:8]]), "%Y-%m-%d %H:%M:%S").hour
            print "{0}\t{1}".format(line[3], hour)
if __name__ == '__main__':
    mapper()