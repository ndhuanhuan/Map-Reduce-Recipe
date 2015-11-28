#!/usr/bin/python

import sys

popular_hits = 0
popular_file = None

hits = 0
old_key = None

for line in sys.stdin:
    key = line.strip()

    if old_key is not None and old_key != key:
        if hits > popular_hits:
            popular_hits = hits
            popular_file = old_key

        old_key = key
        hits = 0

    old_key = key
    hits += 1

if old_key is not None:
    print("{0}\t{1}".format(popular_file, popular_hits))
