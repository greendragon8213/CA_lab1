from news_parser.single_thread import *
import urllib2
from urllib2 import HTTPError
from urllib2 import URLError
from news_parser.multi_thread import *
from time import time
import unit_tests.unit_tests

file_path = "/Users/GreenUser/PycharmProjects/CALab1/sportnews.xml"


final_res = []
urls = find_by_tag('url', file_path)
if len(urls) == 0:
    raise RuntimeError('Urls list is emtpy')
t0 = time()
for url in urls:
    try:
        obj = urllib2.urlopen(url)
    except HTTPError as e:
        print 'Error', e.code
    except URLError as e:
        print 'Reason:', e.reason
    else:
        byte_arr = obj.read(-1)
        temp = parse_rss(byte_arr)
        final_res.extend(temp)
t1 = time()
if len(final_res) == 0:
    raise RuntimeError('final res empty')
write_xml(final_res, "single_thread.xml")
t2 = time()
results = multi_thread_parse(urls)
t3 = time()
write_xml(results, "multi_thread.xml")
print(t1 - t0)
print(t3-t2)
