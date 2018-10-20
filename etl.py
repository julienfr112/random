import os
import sys
#os.system('clickhouse client --query "select * from sensi limit 10000000 format JSONEachRow" > /tmp/data')

"""run with """
"""cat /tmp/data | parallel -X --pipe -L1000000 --block-size 100M python3.6 etl.py"""


import ujson

for l in sys.stdin:
    v = ujson.loads(l)
    print(v["tradeid"])
