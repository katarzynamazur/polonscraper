# !/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import os
import sys
import time
from common.DjangoTemplatesBuilder import DjangoTemplatesBuilder

from common.PathCreator import PathCreator
from common.Worker import Worker
from database_management.POLonDB_AllPhD import POLonDB_AllPhD
from database_management.POLonDB_PhD import POLonDB_PhD
from database_management.POLonDB_PhD import POLonDB_PhD
from dblp.DBLPScraper29072015 import DBLPScraper29072015
from googlescholar.GoogleScholarScraper23072015 import GoogleScholarScraper23072015
from polon.POLonPhDParser import POLonPhDParser
from polon.POLonPhDScraper23072015 import POLonPhDScraper23072015
from scopus.ScopusScraperParser import ScopusScraperSpamer

reload(sys)
sys.setdefaultencoding("utf8")

DEBUG = True


class PhDWorker(Worker):
    def __init__(self):
        Worker.__init__(self)
        self.path_creator = PathCreator()
        self.django_templates = DjangoTemplatesBuilder()

    def __get_files_from_dir(self, path):

        def get_number(path):
            basename = path.partition('.')
            filename = basename[0].split(os.path.sep)[-1]
            a, b, c = filename.split('_')
            return int(c)

        filenames = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and not f.startswith('.')]
        filenames.sort(key=get_number)
        return filenames

    def __read_html_from_file(self, path):
        with open(path, "r") as text_file:
            html = text_file.read()
        return html

    # ###################################################################################################################

    def build_polon_all_database(self, scrap, dbname):

        i = 1

        scraper = POLonPhDScraper23072015()
        parser = POLonPhDParser()

        if scrap:
            scraper.scrap_and_save_to_files(self.path_creator.create_polon_phd_file_path('polon_phd_%s.txt'))

        files = self.__get_files_from_dir(self.path_creator.create_polon_phd_dir_path())

        db_mgmt = POLonDB_AllPhD(self.path_creator.create_polon_phd_db_file_path(dbname))
        db_mgmt.create_table()

        phds = []

        for file in files:
            page = self.__read_html_from_file(file)
            phds = parser.parse(page)

            if DEBUG:
                print "\n"
                sys.stdout.write('-' * 80)
                sys.stdout.write("FILE: " + file)
                sys.stdout.write('-' * 80)
                print "\n"

            for phd in phds:
                db_mgmt.insert(phd)

                if DEBUG:
                    print i, phd
                i += 1

            phds[:] = []

    def build_polon_it_database(self, alldbname, itdbname):

        alldb = POLonDB_AllPhD(self.path_creator.create_polon_phd_db_file_path(alldbname))
        alldb.create_table()

        itdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(itdbname))
        itdb.create_table()

        it_phds = alldb.select_by_discipline('informatyka')
        i = 1
        print len(it_phds)
        for it_phd in it_phds:
            itdb.insert(it_phd)
            print i, it_phd
            i += 1

    def build_polon_math_database(self, alldbname, mathdbname):

        alldb = POLonDB_AllPhD(self.path_creator.create_polon_phd_db_file_path(alldbname))
        alldb.create_table()

        mathdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(mathdbname))
        mathdb.create_table()

        math_phds = alldb.select_by_discipline('matematyka')

        i = 1
        print len(math_phds)
        for math_phd in math_phds:
            mathdb.insert(math_phd)
            print i, math_phd
            i += 1

    def build_polon_it_umcs_database(self, alldbname, it_umcs_dbname):

        alldb = POLonDB_AllPhD(self.path_creator.create_polon_phd_db_file_path(alldbname))
        alldb.create_table()

        itdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(it_umcs_dbname))
        itdb.create_table()

        itlist = [(u"Bartłomiej", u"Bielecki"), (u"Rafał", u"Cebryk"), (u"Michał", u"Chromiak"),
                  (u"Ireneusz", u"Codello"), (u"Andrzej", u"Daniluk"), (u"Marcin", u"Denkowski"),
                  (u"Krzysztof", u"Dmitruk"), (u"Dariusz", u"Dobrowolski"), (u"Marek", u"Góźdź"),
                  (u"Magdalena", u"Granos"), (u"Wiesław", u"Kamiński"), (u"Adam", u"Kobus"), (u"Jerzy", u"Kotliński"),
                  (u"Sławomir", u"Kotyra"), (u"Bartłomiej", u"Kotyra"), (u"Andrzej", u"Krajka"),
                  (u"Jacek", u"Krzaczkowski"), (u"Bogdan", u"Księżopolski"), (u"Karol", u"Kuczyński"),
                  (u"Rajmund", u"Kuduk"), (u"Michał", u"Kufel"), (u"Wiesława", u"Kuniszyk-Jóźkowiak"),
                  (u"Łukasz", u"Kwaśniewicz"), (u"Monika", u"Leśnik"), (u"Beata", u"Lewczuk"),
                  (u"Zdzisław", u"Łojewski"), (u"Katarzyna", u"Mazur"), (u"Paweł", u"Mikołajczak"),
                  (u"Adam", u"Misiura"), (u"Paweł", u"Olszewski"), (u"Ireneusz", u"Panasiuk"), (u"Michał", u"Pańczyk"),
                  (u"Nikodem", u"Polak"), (u"Damian", u"Rusinek"), (u"Łukasz", u"Sadkowski"), (u"Anna", u"Sasak-Okoń"),
                  (u"Marcin", u"Smolira"), (u"Rafał", u"Stęgierski"), (u"Waldemar", u"Suszyński"),
                  (u"Marek", u"Wiśniewski"), (u"Grzegorz", u"Wójcik"), (u"Michał", u"Żukowski"), (u"Tomasz", u"Żurek")]

        i = 1

        for it in itlist:
            phd = alldb.select_by_name(it[0], it[1])
            if not phd.empty() :
                itdb.insert(phd)
                print i, phd
                i += 1

    def build_polon_math_umcs_database(self, alldbname, math_umcs_dbname):

        alldb = POLonDB_AllPhD(self.path_creator.create_polon_phd_db_file_path(alldbname))
        alldb.create_table()

        mathdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(math_umcs_dbname))
        mathdb.create_table()

        mathlist = [(u"Artur", u"Bator"), (u"Anna", u"Bednarska"), (u"Anna", u"Betiuk-Pilarska"),
                    (u"Halina", u"Bielak"), (u"Mariusz", u"Bieniek"), (u"Monika", u"Budzyńska"),
                    (u"Jarosław", u"Bylina"), (u"Beata", u"Bylina"), (u"Tymoteusz", u"Chojecki"),
                    (u"Małgorzata", u"Cudna"), (u"Iwona", u"Ćwiklińska"), (u"Dorota", u"Dudek"),
                    (u"Andrzej", u"Ganczar"), (u"Anna", u"Gąsior"), (u"Janusz", u"Godula"), (u"Kazimierz", u"Goebel"),
                    (u"Ewelina", u"Grabias"), (u"Wiesława", u"Kaczor"), (u"Alina", u"Kargol"),
                    (u"Dorota", u"Kępa-Maksymowicz"), (u"Michał", u"Klisowski"), (u"Tomasz", u"Komorowski"),
                    (u"Stanisław", u"Kotorowicz"), (u"Monika", u"Kotorowicz"), (u"Piotr", u"Kowalski"),
                    (u"Aleksander", u"Kowalski"), (u"Agnieszka", u"Kozak-Prus"), (u"Jurij", u"Kozicki"),
                    (u"Łukasz", u"Kruk"), (u"Andrzej", u"Kryczka"), (u"Tadeusz", u"Kuczumow"), (u"Artur", u"Kukuryka"),
                    (u"Jan", u"Kurek"), (u"Katarzyna", u"Kwaśnik"), (u"Bartosz", u"Łanucha"),
                    (u"Przemysław", u"Matuła"), (u"Małgorzata", u"Michalska"), (u"Witold", u"Mozgawa"),
                    (u"Jerzy", u"Mycka"), (u"Maria", u"Nowak"), (u"Dorota", u"Pańczyk"), (u"Piotr", u"Pawlas"),
                    (u"Łukasz", u"Piasecki"), (u"Monika", u"Piekarz"), (u"Piotr", u"Pikuta"),
                    (u"Mariusz", u"Plaszczyk"), (u"Joanna", u"Potiopa"), (u"Bolesław", u"Prus"),
                    (u"Stanisław", u"Prus"), (u"Zbigniew", u"Radziszewski"), (u"Beata", u"Rodzik"),
                    (u"Massimiliano", u"Rosini"), (u"Zdzisław", u"Rychlik"), (u"Magdalena", u"Skrzypiec"),
                    (u"Urszula", u"Skwara"), (u"Paweł", u"Sobolewski"), (u"Przemysław", u"Stpiczyński"),
                    (u"Robert", u"Suprynowicz"), (u"Mariusz", u"Szczepanik"), (u"Vasyl", u"Ustymenko"),
                    (u"Anna", u"Walczuk"), (u"Tomasz", u"Walczyński"), (u"Przemysław", u"Widelski"),
                    (u"Anna", u"Wolińska-Welcz"), (u"Magdalena", u"Wołoszkiewicz-Cyll"), (u"Aneta", u"Wróblewska"),
                    (u"Wiesław", u"Zięba")]

        i = 1

        for it in mathlist:
            phd = alldb.select_by_name(it[0], it[1])
            if not phd.empty() :
                mathdb.insert(phd)
                print i, phd
                i += 1

    ####################################################################################################################

    def get_google_scholar_info(self, itdbname):

        itdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(itdbname))
        itdb.create_table()

        google_scraper = GoogleScholarScraper23072015('https://scholar.google.com/citations?view_op=search_authors')

        len = itdb.get_number_of_all_phds()

        print len
        id = 1

        for i in range(0, len):
            phd = itdb.select_by_id(id)
            hindex, citations = google_scraper.get_hindex_and_citations(phd.firstname, phd.lastname)
            itdb.update_google_scholar(phd, citations, hindex)
            phd = itdb.select_by_id(id)
            print phd.to_string()
            id += 1
            time.sleep(200)

            # if DEBUG:
            # print "%s %s Hindex: %s, Citations: %s" % (phd.firstname, phd.lastname, hindex, citations)

    ####################################################################################################################

    def get_dblp_num_of_all_pubs_info(self, itdbname):

        itdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(itdbname))
        itdb.create_table()

        dblp_scraper = DBLPScraper29072015()

        len = itdb.get_number_of_all_phds()
        id = 1

        for i in range(0, len):
            phd = itdb.select_by_id(id)
            num_of_pubs = dblp_scraper.get_number_of_publications(phd.firstname, phd.lastname)
            itdb.update_dblp_num_of_all_pubs(phd, num_of_pubs)
            phd = itdb.select_by_id(id)
            print phd.to_string()
            id += 1
            time.sleep(200)

    ####################################################################################################################

    def get_scopus_num_of_all_pubs_info(self, itdbname, keyword):

        itdb = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(itdbname))
        itdb.create_table()

        scopus = ScopusScraperSpamer()

        len = itdb.get_number_of_all_phds()
        id = 1

        for i in range(0, len):
            phd = itdb.select_by_id(id)

            num_of_pubs = scopus.get_number_of_publications(phd.firstname, phd.lastname, 'comp')
            hindex = scopus.get_hindex(phd.firstname, phd.lastname, 'comp')

            itdb.update_scopus(phd, num_of_pubs, hindex)
            phd = itdb.select_by_id(id)

            print phd.to_string()

            id += 1
            time.sleep(200)

    ####################################################################################################################

    def build_django_html_google_scholar_citations(self, dbname, type=None):
        return self.django_templates.build_html_google_scholar_citations(dbname, type)

    def build_django_html_google_scholar_hindex(self, dbname, type=None):
        return self.django_templates.build_html_google_scholar_hindex(dbname, type)

    def build_django_html_dblp_num_of_pubs(self, dbname, type=None):
        return self.django_templates.build_html_dblp_num_of_pubs(dbname, type)

    def build_django_html_scopus_hindex(self, dbname, type=None):
        return self.django_templates.build_html_scopus_hindex(dbname, type)

    def build_django_html_scopus_num_of_pubs(self, dbname, type=None):
        return self.django_templates.build_html_scopus_num_of_pubs(dbname, type)

    ####################################################################################################################


if __name__ == "__main__":
    w = PhDWorker()

    # w.build_polon_all_database(False, 'POLon_PhD_All_DB.sql')
    # w.build_polon_it_database('POLon_PhD_All_DB.sql', 'POLon_PhD_IT_DB.sql')
    # w.build_polon_math_database('POLon_PhD_All_DB.sql', 'POLon_PhD_MATH_DB.sql')
    # w.build_polon_math_umcs_database('POLon_PhD_All_DB.sql', 'POLon_PhD_MATH_UMCS_DB.sql')
    w.build_polon_it_umcs_database('POLon_PhD_All_DB.sql', 'POLon_PhD_IT_UMCS_DB.sql')

    # w.get_google_scholar_info('POLon_PhD_IT_DB.sql')
    # w.get_dblp_num_of_all_pubs_info('POLon_PhD_IT_DB.sql')
    # w.get_scopus_num_of_all_pubs_info('POLon_PhD_IT_DB.sql')
    #
    # w.get_google_scholar_info('POLon_PhD_MATH_DB.sql')
    # w.get_dblp_num_of_all_pubs_info('POLon_PhD_MATH_DB.sql')
    # w.get_scopus_num_of_all_pubs_info('POLon_PhD_MATH_DB.sql')

    #
    # print w.build_django_html_scopus_hindex('POLon_PhD_IT_DB.sql', 'drhab')
    # print w.build_django_html_scopus_hindex('POLon_PhD_IT_DB.sql', 'dr')
    # print w.build_django_html_scopus_hindex('POLon_PhD_IT_DB.sql')

    # print w.build_django_html_scopus_num_of_pubs('POLon_PhD_IT_DB.sql', 'drhab')
    # print w.build_django_html_scopus_num_of_pubs('POLon_PhD_IT_DB.sql', 'dr')
    # print w.build_django_html_scopus_num_of_pubs('POLon_PhD_IT_DB.sql')

    # print w.build_django_html_google_scholar_citations('POLon_PhD_IT_DB.sql', 'drhab')
    # print w.build_django_html_google_scholar_citations('POLon_PhD_IT_DB.sql', 'dr')
    # print w.build_django_html_google_scholar_citations('POLon_PhD_IT_DB.sql')

    # print w.build_django_html_google_scholar_hindex('POLon_PhD_IT_DB.sql', 'drhab')
    # print w.build_django_html_google_scholar_hindex('POLon_PhD_IT_DB.sql', 'dr')
    # print w.build_django_html_google_scholar_hindex('POLon_PhD_IT_DB.sql')

    # print w.build_django_html_dblp_num_of_pubs('POLon_PhD_IT_DB.sql', 'drhab')
    # print w.build_django_html_dblp_num_of_pubs('POLon_PhD_IT_DB.sql', 'dr')
    # print w.build_django_html_dblp_num_of_pubs('POLon_PhD_IT_DB.sql')
