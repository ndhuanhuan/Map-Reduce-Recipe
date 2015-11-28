#! /usr/bin/python

import sys
import heapq
K = 10
def reducer():
    
    heap = []
    
    access_count = 0
    old_key = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue
    
        this_key, this_access = data_mapped
    
        if old_key and old_key != this_key:
            count_key_tuple = (access_count, old_key)
            if len(heap) < K or count_key_tuple > heap[0]:
                if len(heap) == K:
                    heapq.heappop(heap)
                heapq.heappush(heap, count_key_tuple)
                
            #print("{0}\t{1}".format(old_key, acces_count))
            old_key = this_key
            access_count = 0
    
        old_key = this_key
        access_count += float(this_access)
    
    if old_key is not None:
        count_key_tuple = (access_count, old_key)
        if len(heap) < K or count_key_tuple > heap[0]:
            if len(heap) == K:
                heapq.heappop(heap)
            heapq.heappush(heap, count_key_tuple)
    for item in heap:
        print("{0}\t{1}".format(item[1], item[0]))
if __name__ == "__main__":
    reducer()
