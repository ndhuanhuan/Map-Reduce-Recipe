#!/usr/bin/python
import operator
import sys
def reducer():
    old_key = None
    hour_dict = dict()
    most_hour = 0
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        this_key, this_hour = data # key is author_id, this_hour is hour for this post and this author
        if old_key and old_key != this_key: # time to change
            sorted_hour_dict = sorted(hour_dict.items(), reverse=True, key=operator.itemgetter(1))
            most_hour = sorted_hour_dict[0][0]
            print "{0}\t{1}".format(old_key, most_hour)
            # return to initial
            old_key = this_key
            hour_dict = dict()
            most_hour = 0

        old_key = this_key
        hour_dict[this_hour] = hour_dict.get(this_hour, 0) + 1
    if old_key is not None: # the final data (last author_id's data) from map
        sorted_hour_dict = sorted(hour_dict.items(), reverse=True, key=operator.itemgetter(1))
        most_hour = sorted_hour_dict[0][0]
        print "{0}\t{1}".format(old_key, most_hour)        

if __name__ == '__main__':
    reducer()    