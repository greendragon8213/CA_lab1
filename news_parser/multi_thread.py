import gevent
from gevent import monkey
import itertools
from single_thread import *
import urllib2

monkey.patch_all()


def get_urls_contents(urls):
    urls_tasks = [gevent.spawn(urllib2.urlopen(url).read, -1) for url in urls]
    gevent.joinall(urls_tasks)
    return urls_tasks


def multi_thread_parse(urls, tasks_joiner=get_urls_contents):
    urls_tasks = tasks_joiner(urls)
    tasks = [gevent.spawn(parse_rss, url.value) for url in urls_tasks]
    gevent.joinall(tasks)
    return list(itertools.chain.from_iterable([t.value for t in tasks]))
