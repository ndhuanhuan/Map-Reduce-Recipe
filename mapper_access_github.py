#!/usr/bin/python

import sys
import re

regex_log = re.compile("(?P<host>\S+) (?P<identity>\S+) (?P<username>\S+) \[(?P<time>.+)\] \"(?P<method>.+) "
                       "(?P<request>.+) (?P<protocol>.+)\" (?P<status>[0-9]+) (?P<size>\S+)")

regex_fname = re.compile("http://.*?(/.*)")

for line in sys.stdin:
    r = regex_log.search(line)
    if r is not None:
        res_log = r.groupdict()
        request = res_log[u'request']
        if request.startswith('http'):
            res_fname = regex_fname.findall(request)
            if res_fname is not None and len(res_fname) > 0:
                print(res_fname[0])
        else:
            print(request)
