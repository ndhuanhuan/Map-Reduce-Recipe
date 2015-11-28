#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
def reducer():
    totalSalesPerDay = 0
    totalWeekday = 0
    oldKey = None
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        thisKey, thisSale = data
        if oldKey and oldKey != thisKey:
            #it's time to print the result
            print "{0}\t{1}".format(oldKey, totalSalesPerDay)
            totalSalesPerDay = 0
            totalWeekday = 0
            
        oldKey = thisKey
        totalSalesPerDay += float(thisSale)
        totalWeekday += 1
        
    if oldKey != None:
        print "{0}\t{1}".format(oldKey, totalSalesPerDay)
        
if __name__ == '__main__':
    reducer()