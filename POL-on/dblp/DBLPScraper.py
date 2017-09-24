# !/usr/bin/env python
# -*- coding: utf-8 -*-

class DBLPScraper(object):
    def __init__(self):
        self.DBLP_BASE_URL = 'http://dblp.uni-trier.de/'
        self.DBLP_AUTHOR_SEARCH_URL = self.DBLP_BASE_URL + 'search/author'
        self.DBLP_PERSON_URL = self.DBLP_BASE_URL + 'pers/xk/{urlpt}'
        self.DBLP_PUBLICATION_URL = self.DBLP_BASE_URL + 'rec/bibtex/{key}.xml'

    def get_publications(self, firstname, lastname):
        """
        """

    def get_number_of_publications(self, firstname, lastname):
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
