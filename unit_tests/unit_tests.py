import unittest
from news_parser.single_thread import *
from news_parser.multi_thread import *
import xml.etree.ElementTree as ET

file = open("/Users/GreenUser/PycharmProjects/CALab1/fortest.txt", 'r')
asd = file.read()
for_test = ET.fromstring(asd)
item_for_test = for_test.find('.//item')
items = [txt for txt in for_test.findall('.//item')]
filtered_items = [i for i in items if contains_score(i)]
urls = find_by_tag('url', "/Users/GreenUser/PycharmProjects"
                          "/CALab1/sportnews.xml")


class test_single_thread(unittest.TestCase):
    def test_find_by_tag(self):
        self.assertEqual(find_by_tag('url', "/Users/GreenUser"
                                            "/PycharmProjects"
                                            "/CALab1/sportnews.xml"),
                         ['http://sports.yahoo.com/'
                          'soccer//rss.xml',
                          'http://feeds.news.com.au/public'
                          '/rss/2.0/fs_football_20.xml',
                          'http://www.espnfc.com/rss',
                          'http://www.espn.co.uk/rss/sport/story'
                          '/feeds/0.xml?sport=3;type=2'])

    def test_contains_score(self):
        self.assertEqual(contains_score(item_for_test), False)

    def test_write_xml(self):
        self.assertEqual(write_xml(item_for_test, "UT.xml"), True)

    def test_multi_thread_parse(self):
        test = multi_thread_parse(urls, mock_data)
        result = filtered_items*4
        self.assertEqual(len(test), len(result))


class geventMock:
    def __init__(self):
        self.value = asd


def mock_data(urls):
    return [geventMock() for _ in range(len(urls))]

suite = unittest.TestLoader().loadTestsFromTestCase(test_single_thread)
unittest.TextTestRunner(verbosity=2).run(suite)
