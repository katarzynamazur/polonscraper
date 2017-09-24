#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2

from bs4 import BeautifulSoup
import mechanize
import sys

reload(sys)
sys.setdefaultencoding("utf8")
from googlescholar.GoogleScholarScraper import GoogleScholarScraper


class GoogleScholarScraper23072015(GoogleScholarScraper):
    def __init__(self, site_url):
        GoogleScholarScraper.__init__(self, site_url)

    def get_citations(self, firstname, lastname):
        author_profile_page = self.__scrap_author_page(firstname, lastname)
        if author_profile_page is not None:
            citations = self.__scrap_citations(author_profile_page)
            if citations is not None:
                return citations
        return -1

    def get_hindex(self, firstname, lastname):
        author_profile_page = self.__scrap_author_page(firstname, lastname)
        if author_profile_page is not None:
            hindex = self.__scrap_hindex(author_profile_page)
            if hindex is not None:
                return hindex
        return -1

    def get_hindex_and_citations(self, firstname, lastname):
        author_profile_page = self.__scrap_author_page(firstname, lastname)
        if author_profile_page is not None:
            citations, hindex = self.__scrap_hindex_and_citations(author_profile_page)
            if citations is not None and hindex is not None:
                return hindex, citations
        return -1, -1

    def __scrap_hindex_and_citations(self, html):
        """
        Scraps and returns a tuple consisting of
        citations (in total - element 0) and
        hindex (in total - element 1) from
        author's profile page
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            tds = soup.find_all("td", {"class": "gsc_rsb_std"})
            citations = int(tds[0].text)
            hindex = int(tds[2].text)
            return citations, hindex
        except:
            return -1, -1

    def __scrap_hindex(self, html):
        """
        Scraps and returns hindex (in total)
        from author's profile page
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            tds = soup.find_all("td", {"class": "gsc_rsb_std"})
            return int(tds[2].text)
        except:
            return -1

    def __scrap_citations(self, html):
        """
        Scraps and returns citations (in total)
        from author's profile page
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            tds = soup.find_all("td", {"class": "gsc_rsb_std"})
            return int(tds[0].text)
        except:
            return -1

    def __scrap_author_page(self, firstname, lastname):
        author_page_from_search_results = self.__find_author_page_in_search_results(firstname, lastname)
        if author_page_from_search_results is not None:
            url = self.__find_author_profile_link(author_page_from_search_results, firstname, lastname)
            if url is not None:
                html = self.__get_author_profile_page_source(url)
                if html is not None:
                    return html
        return None

    def __find_author_page_in_search_results(self, firstname, lastname):

        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.addheaders = [('User-Agent',
                               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17'),
                              ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                              ('Accept-Language', 'en-US,en;q=0.8,ru;q=0.6'),
                              ('Cache-Control', 'max-age=0'),
                              ('Connection', 'keep-alive')]

        firstname = firstname.title()
        lastname = lastname.title()

        try:

            html = browser.open(self.site_url)
            author_search_field = self.__find_search_input(browser)

            if author_search_field is not None:
                author_search_field.value = firstname + " " + lastname
                browser.select_form(nr=0)
                result_page = browser.submit(id="gs_hdr_tsb")
                html = result_page.read()
                browser.close()
                return html
        except Exception, e:
            print str(e)
            return None

        return None

    def __find_author_profile_link(self, author_page_from_search_results, firstname, lastname):
        """
        Returns first matching link to authors profile
        """

        base_link = 'https://scholar.google.com'
        author_link = ''

        # from page with search results, get a list of authors and profile links
        profiles = self.__find_authors_and_links(author_page_from_search_results)

        if profiles is not None:

            # for every found author
            for profile in profiles:

                # check if name from DB matches the name from google scholar
                match = self.__check_if_names_match(profile, firstname, lastname)

                # if names match, we have the profile link
                if match:
                    author_link = profile[1]
                    break

            # return full link to google scholar profile
            return base_link + author_link

        return None

    def __find_authors_and_links(self, author_page_from_search_results):
        """
        Finds all the authors and links to their google scholar
        profiles, returned by the browser after searching given name
        """

        try:
            authors = []
            soup = BeautifulSoup(author_page_from_search_results, 'html.parser')
            author_links = soup.find_all('a', href=True)
            for author_link in author_links:
                imgs = author_link.find_all("img")
                for img in imgs:
                    authors.append((img['alt'], author_link['href']))
            return authors
        except:
            return None

    def __find_search_input(self, browser):
        """
        Finds and returns search control - input where
        one can type author's name
        """
        forms = browser.forms()
        for form in forms:
            controls = form.controls
            for control in controls:
                if control.name == "mauthors" and control.type == "text" and control.id == "gs_hdr_frm_in_txt":
                    author_search_field = control
                    return author_search_field
        return None

    def __find_search_button(self, browser):
        forms = browser.forms()
        for form in forms:
            controls = form.controls
            for control in controls:
                if control.type == "submitbutton" and control.id == "gs_hdr_tsb":
                    search_button = control
                    return search_button
        return None

    def __get_author_profile_page_source(self, url):
        bad = True
        while bad:
            try:
                page = urllib2.urlopen(url)
                return page.read()
            except:
                pass
        return None

    def __replace_polish_letters(self, text):
        text = text.replace("ł", "l")
        text = text.replace("ś", "s")
        text = text.replace("ą", "a")
        text = text.replace("ę", "e")
        text = text.replace("ó", "o")
        text = text.replace("ń", "n")
        text = text.replace("ż", "z")
        text = text.replace("ź", "z")
        return text

    def __check_if_names_match(self, profile, firstname, lastname):

        # name 1 - from google scholar profile
        firstnamelastname = profile[0]
        firstnamelastname = firstnamelastname.replace(" ", "")
        firstnamelastname = firstnamelastname.lower()

        # name 2 - provided by the user (from DB actually)
        concat_firstname_lastname = firstname.lower() + lastname.lower()

        if self.__replace_polish_letters(firstnamelastname) == self.__replace_polish_letters(concat_firstname_lastname):
            return True

        return False


if __name__ == "__main__":
    google_scraper = GoogleScholarScraper23072015('https://scholar.google.com/citations?view_op=search_authors')
    print google_scraper.get_hindex_and_citations('zbigniew', 'kotulski')
    print google_scraper.get_hindex_and_citations('bogdan', 'ksiezopolski')
    # print google_scraper.get_hindex_and_citations('katarzyna', 'mazur')
    # print google_scraper.get_hindex_and_citations('damian', 'rusinek')
    # print google_scraper.get_hindex_and_citations('adam', 'wierzbicki')
