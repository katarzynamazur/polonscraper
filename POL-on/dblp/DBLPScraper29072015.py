# !/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree

import requests

from dblp.DBLPScraper import DBLPScraper


class DBLPScraper29072015(DBLPScraper):
    def __init__(self):
        DBLPScraper.__init__(self)

    def __build_name_string(self, firstname, lastname):
        return "%s:%s" % (firstname.title(), lastname.title())

    def __get_response(self, url, params=None):
        try:
            response = requests.get(url, params=params)
            return response
        except requests.exceptions.Timeout as e:
            print e
            return None
        except requests.exceptions.TooManyRedirects as e:
            print e
            return None
        except requests.exceptions.RequestException as e:
            print e
            return None

    def __get_urlpts_for_name(self, firstname, lastname):
        name_string = self.__build_name_string(firstname, lastname)
        response = self.__get_response(self.DBLP_AUTHOR_SEARCH_URL, {'xauthor': name_string})
        if response is not None:
            try:
                root = etree.fromstring(response.content)
                urlpts = [urlpt for urlpt in root.xpath('/authors/author/@urlpt')]
                return urlpts
            except etree.XMLSyntaxError as e:
                print e
                return None

    def __get_publication_page(self, urlpt):
        return self.__get_response(self.DBLP_PERSON_URL.format(urlpt=urlpt))

    def __get_number_of_publications(self, urlpt):
        num_of_pubs = 0
        pub_page = self.__get_publication_page(urlpt)
        if pub_page is not None:
            try:
                root = etree.fromstring(pub_page.content)
                for child in root.getchildren():
                    if not child.attrib:
                        num_of_pubs += 1
            except etree.XMLSyntaxError as e:
                print e
                return -1
        return num_of_pubs

    def get_number_of_publications(self, firstname, lastname):
        urlpts = self.__get_urlpts_for_name(firstname, lastname)
        if urlpts is not None and len(urlpts) > 0:
            # we consider only the first found urlpt (author) so there can be some mistakes
            num_of_pubs = self.__get_number_of_publications(urlpts[0])
            return num_of_pubs
        return -1

    def get_publications(self, firstname, lastname):
        """
        """

    def get_number_of_books_and_theses(self, firstname, lastname):
        """
        """

    def get_number_of_journal_articles(self, firstname, lastname):
        """
        """

    def get_number_of_conference_and_workshop_papers(self, firstname, lastname):
        """
        """

    def get_number_of_parts_in_books_or_collections(self, firstname, lastname):
        """
        """

    def get_number_of_editorship(self, firstname, lastname):
        """
        """

    def get_number_of_reference_works(self, firstname, lastname):
        """
        """

    def get_number_of_informal_and_other_publications(self, firstname, lastname):
        """
        """


if __name__ == "__main__":
    dblp_scraper = DBLPScraper29072015()
    # print dblp_scraper.get_number_of_publications('Michael', 'Ley')
    print dblp_scraper.get_number_of_publications('Ksiezopolski', 'Bogdan')
