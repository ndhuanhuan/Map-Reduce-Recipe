# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:20:49 2015

@author: hehe
"""

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
            print "{0}\t{1}\t{2}\t{3}".format(oldKey, totalSalesPerDay, totalWeekday, totalSalesPerDay/totalWeekday)
            totalSalesPerDay = 0
            totalWeekday = 0
            
        oldKey = thisKey
        totalSalesPerDay += float(thisSale)
        totalWeekday += 1
        
    if oldKey != None:
        print "{0}\t{1}\t{2}\t{3}".format(oldKey, totalSalesPerDay, totalWeekday, totalSalesPerDay/totalWeekday)
        
if __name__ == '__main__':
    reducer()