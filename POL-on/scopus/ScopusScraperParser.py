# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class ScopusScraperSpamer(object):
    def __init__(self):

        self.SCOPUS_API_KEY = "def2a8aa2b91e77547ecef7299843c9b"

        self.headers = {'Accept': 'application/json', 'X-ELS-APIKey': self.SCOPUS_API_KEY}

        self.AUTHOR_SEARCH_BASE_URL = "http://api.elsevier.com/content/search/author?"
        self.AUTHOR_SEARCH_API_KEY_URL = "http://api.elsevier.com/content/search/author?apiKey=%s&" % (
            self.SCOPUS_API_KEY)

        self.AUTHORS_ARTICLES_SEARCH_BASE_URL = "http://api.elsevier.com/content/search/scopus?"
        self.AUTHORS_ARTICLES_API_KEY_URL = "http://api.elsevier.com/content/search/scopus?apiKey=%s&" % (
            self.SCOPUS_API_KEY)

    def __build_author_search_query_url(self, firstname, lastname, discipline, with_api_key=True):
        firstname = firstname.title()
        lastname = lastname.title()
        search_query = "query=AUTHFIRST(%s) AND AUTHLASTNAME(%s) AND SUBJAREA(%s)" % (firstname, lastname, discipline)
        search_url = None
        if not with_api_key:
            search_url = self.AUTHOR_SEARCH_BASE_URL + search_query
        else:
            search_url = self.AUTHOR_SEARCH_API_KEY_URL + search_query
        return search_url

    def __build_authors_articles_search_query(self, author_id, with_api_key=True):
        search_query = "query=AU-ID(%s)&field=dc:identifier&" % (author_id)
        search_url = None
        if not with_api_key:
            search_url = self.AUTHORS_ARTICLES_SEARCH_BASE_URL + search_query
        else:
            search_url = self.AUTHORS_ARTICLES_API_KEY_URL + search_query
        return search_url

    def __build_authors_metrics_url(self, author_id, with_api_key=True):
        search_query = "author_id=%s&view=metrics" % (author_id)
        return "http://api.elsevier.com/content/author?author_id=%s&view=metrics&apiKey=%s&" % (
        author_id, self.SCOPUS_API_KEY)

    def __make_request(self, url, headers):
        page_request = None
        try:
            page_request = requests.get(url, headers=headers)
            page_request = page_request.json()
        except requests.exceptions.Timeout:
            return None
        except requests.exceptions.TooManyRedirects:
            return None
        except requests.exceptions.RequestException as e:
            return None
        return page_request

    def __get_author_page_xml(self, firstname, lastname, discipline):
        author_search_url = self.__build_author_search_query_url(firstname, lastname, discipline)
        return self.__make_request(author_search_url, self.headers)

    def __get_author_id(self, author_page_xml):
        try:
            return str(
                [[str(element['dc:identifier'])] for element in author_page_xml['search-results']["entry"]][0][0].split(
                    ":")[1])
        except:
            return -1

    def get_author_id(self, firstname, lastname, discipline):
        author_page_xml = self.__get_author_page_xml(firstname, lastname, discipline)
        if author_page_xml is not None:
            return self.__get_author_id(author_page_xml)
        return -1

    def __get_publications_ids(self, firstname, lastname, discipline):
        id = self.get_author_id(firstname, lastname, discipline)
        if id != -1:
            publications_url = self.__build_authors_articles_search_query(id)
            response = self.__make_request(publications_url, self.headers)
            if response is not None:
                try:
                    return [[str(r['dc:identifier'])] for r in response['search-results']["entry"]]
                except:
                    return None
        return None

    def get_publications_ids(self, firstname, lastname, discipline):
        return self.__get_publications_ids(firstname, lastname, discipline)

    def __get_hindex_author_metrics(self, firstname, lastname, discipline):
        author_id = self.get_author_id(firstname, lastname, discipline)
        if author_id != -1:
            authors_metrics_url = self.__build_authors_metrics_url(author_id)
            response = self.__make_request(authors_metrics_url, self.headers)
            if response is not None:
                try:
                    return response['author-retrieval-response'][0]['h-index']
                except:
                    return -1
        return -1

    def get_hindex(self, firstname, lastname, discipline):
        return self.__get_hindex_author_metrics(firstname, lastname, discipline)

    def __get_number_of_publications(self, firstname, lastname, discipline):
        publications = self.__get_publications_ids(firstname, lastname, discipline)
        if publications is None:
            return 0
        return len(publications)

    def __get_number_of_publications_author_metrics(self, firstname, lastname, discipline):
        author_id = self.get_author_id(firstname, lastname, discipline)
        if author_id != -1:
            authors_metrics_url = self.__build_authors_metrics_url(author_id)
            response = self.__make_request(authors_metrics_url, self.headers)
            if response is not None:
                try:
                    return response['author-retrieval-response'][0]['coredata']['document-count']
                except:
                    return -1
        return -1

    def get_number_of_publications(self, firstname, lastname, discipline):
        return self.__get_number_of_publications(firstname, lastname, discipline)


if __name__ == "__main__":
    scopus = ScopusScraperSpamer()
    print scopus.get_number_of_publications('Bogdan', 'Ksiezopolski', 'comp')
    print scopus.get_hindex('Bogdan', 'Ksiezopolski', 'comp')
