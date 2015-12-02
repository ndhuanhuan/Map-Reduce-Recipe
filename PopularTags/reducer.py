#!/usr/bin/python
import sys
import heapq
def reducer():
    old_key = None
    tag_count = 0
    heap = []
    K = 10
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 2:
            this_key, this_count = data
            if old_key and old_key != this_key:
                # time to change
                count_and_tag = (tag_count, old_key)

                if len(heap) < K or count_and_tag > heap[0]:
                    if len(heap) == K:
                        heapq.heappop(heap)
                    heapq.heappush(heap, count_and_tag)
                # restore to zero                    
                tag_count = 0
                old_key = this_key
            #not changing in this step
            old_key = this_key
            tag_count += 1

    if old_key is not None:
        count_and_tag = (tag_count, old_key)
        if len(heap) < K or count_and_tag > heap[0]:
            if len(heap) == K:
                heapq.heappop(heap)
            heapq.heappush(heap, count_and_tag)
    heap.sort(reverse=True)
    for item in heap:
        print "{0}\t{1}".format(item[1],item[0])
def reducer2():
    old_key = None
    tag_count = 0
    for line in sys.stdin:
        data = line.strip().split('\t')        
        if len(data) == 2:
            this_key, this_count = data
            if old_key and old_key != this_key:
                print "{0}\t{1}".format(old_key, tag_count)
                old_key = None
                tag_count = 0
            old_key = this_key
            tag_count += 1
    if old_key is not None:
        print "{0}\t{1}".format(old_key, tag_count)
if __name__ == '__main__':
    reducer()        