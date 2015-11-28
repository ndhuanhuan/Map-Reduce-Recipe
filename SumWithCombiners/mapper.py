#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
def mapper():
    for line in sys.stdin:
        data = line.rstrip().split('\t')
        weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, data[4])

if __name__ == '__main__':
    mapper()
    