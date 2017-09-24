# !/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree

import requests

DBLP_BASE_URL = 'http://dblp.uni-trier.de/'
DBLP_AUTHOR_SEARCH_URL = DBLP_BASE_URL + 'search/author'
DBLP_PERSON_URL = DBLP_BASE_URL + 'pers/xk/{urlpt}'
DBLP_PUBLICATION_URL = DBLP_BASE_URL + 'rec/bibtex/{key}.xml'


def build_name_string(firstname, lastname):
    return "%s:%s" % (firstname.title(), lastname.title())


def get_urlpts_for_name(firstname, lastname):
    try:
        name_string = build_name_string(firstname, lastname)
        response = requests.get(DBLP_AUTHOR_SEARCH_URL, params={'xauthor': name_string})
        root = etree.fromstring(response.content)
        urlpts = [urlpt for urlpt in root.xpath('/authors/author/@urlpt')]
        return urlpts
    except requests.exceptions.Timeout as e:
        print e
        return None
    except requests.exceptions.TooManyRedirects as e:
        print e
        return None
    except requests.exceptions.RequestException as e:
        print e
        return None


def first_or_none(seq):
    try:
        return next(iter(seq))
    except StopIteration:
        pass


ul = get_urlpts_for_name('ley', 'michael')

# DBLP_PERSON_URL = DBLP_BASE_URL + 'pers/xk/%s' % (str(ul[0]))
# print DBLP_PERSON_URL

resp = requests.get(DBLP_PERSON_URL.format(urlpt=str(ul[0])))
print resp.url

# root = etree.fromstring(resp.content)
# # print root
# for e in root.getchildren():
#     # print e.tag, e.text
#     pub = e.text
#
# tst = [elem for elem in root.getchildren()]
# print tst

# #
# resp = requests.get(DBLP_PUBLICATION_URL.format(key=str(e.text)))
# print resp.url
# xml = resp.content
# # print xml
# root = etree.fromstring(xml)
# for e in root.getchildren():
#     art = e.tag  #, e.text
#     print art
#     for ee in e.getchildren():
#         print ee.tag, ee.text

txt = 'Katarzyna'
t = txt.split()
print t[0]
