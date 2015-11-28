#! /usr/bin/python

import sys

def reducer():
    access_count = 0
    old_key = None
    max_access = 0
    max_access_key = None
    
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue
    
        this_key, this_access = data_mapped
    
        if old_key and old_key != this_key:
            if access_count > max_access:
                max_access = access_count
                max_access_key = old_key
            #print("{0}\t{1}".format(old_key, acces_count))
            old_key = this_key
            access_count = 0
    
        old_key = this_key
        access_count += float(this_access)
    
    if old_key is not None:
        if access_count > max_access:
            max_access = access_count
            max_access_key = old_key        
        print("{0}\t{1}".format(max_access_key, max_access))

if __name__ == "__main__":
    reducer()
