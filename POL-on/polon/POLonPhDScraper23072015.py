# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

from bs4 import BeautifulSoup
import mechanize
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from common.PathCreator import PathCreator
from polon.POLonScraper import POLonScraper

reload(sys)
sys.setdefaultencoding("utf8")


class POLonPhDScraper23072015(POLonScraper):
    def __init__(self, site='https://polon.nauka.gov.pl/opi/aa/drh/zestawienie?execution=e1s1'):
        POLonScraper.__init__(self, site)
        self.num_of_all_pages = self.__get_num_of_all_pages(self.site)

    def scrap(self):
        pages = []
        i = 1

        # prepare browser
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.site)
        wait = WebDriverWait(driver, 30)
        time.sleep(2)

        bad = True
        while bad:
            try:
                # paginate by 100
                select = Select(driver.find_element_by_id("filter:drhPageTable:j_idt162:j_idt165:j_idt171"))
                select.select_by_visible_text("100")
                bad = False
            except:
                pass

        while True:

            # wait until there is no loading spinner
            wait.until(EC.invisibility_of_element_located((By.ID, "loadingPopup_content_scroller")))
            time.sleep(1)

            # get next page number
            # current_page = driver.find_element_by_class_name("rf-ds-act").text
            # print("Current page: %s" % str(current_page))

            #  collect results - pages
            page = driver.page_source
            pages.append(page)

            i += 1

            # proceed to the next page
            try:
                next_page = driver.find_element_by_link_text(u"»")
                next_page.click()
            except NoSuchElementException:
                break

        driver.close()

        return pages

    def save_to_files(self, pages, path):

        i = 1
        for page in pages:
            with open(path % i, "w") as text_file:
                text_file.write(page)
            i += 1

    def scrap_and_save_to_files(self, path):

        pages = []
        i = 1

        # prepare browser
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.site)
        wait = WebDriverWait(driver, 30)
        time.sleep(2)

        bad = True
        while bad:
            try:
                # paginate by 100
                select = Select(driver.find_element_by_id("filter:drhPageTable:j_idt162:j_idt165:j_idt171"))
                select.select_by_visible_text("100")
                bad = False
            except:
                pass

        while True:

            # wait until there is no loading spinner
            wait.until(EC.invisibility_of_element_located((By.ID, "loadingPopup_content_scroller")))
            time.sleep(1)

            # get next page number
            current_page = driver.find_element_by_class_name("rf-ds-act").text
            print("Current page: %s" % str(current_page))

            #  collect results - pages
            page = driver.page_source
            pages.append(page)

            # save pages to files
            with open(path % i, "w") as text_file:
                text_file.write(page)

            i += 1

            # proceed to the next page
            try:
                next_page = driver.find_element_by_link_text(u"»")
                next_page.click()
            except NoSuchElementException:
                break

        driver.close()

        return pages

    def __get_num_of_all_pages(self, site):
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.addheaders = [('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36     (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'),
                              ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                              ('Accept-Language', 'en-US,en;q=0.8,ru;q=0.6'),
                              ('Cache-Control', 'max-age=0'),
                              ('Connection', 'keep-alive')]

        html = browser.open(site)
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all('span', attrs={'style': 'margin-left: 20px;'})[0].text
        result = result.split()
        result = int(result[-2] + result[-1])
        result = round(result / 25) + 1
        browser.close()
        return int(result)


if __name__ == "__main__":
    pc = PathCreator()
    path = pc.create_polon_phd_file_path('polon_phd_%s.txt')

    scraper = POLonPhDScraper23072015()
    # scraper.scrap_and_save_to_files(path)
    scraper.scrap()
