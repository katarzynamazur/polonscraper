# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf8")


class Scientist:
    def __init__(self, firstname='', lastname='', academic_degree='', discipline='',
                 home_university='', work_university='', num_of_pub_dblp='',
                 hindex_google_scholar='', num_of_citations_google_scholar='',
                 num_of_pub_scopus='', hindex_scopus=''):
        self.firstname = firstname
        self.lastname = lastname
        self.academic_degree = academic_degree
        self.discipline = discipline
        self.home_university = home_university
        self.work_university = work_university
        self.num_of_pub_dblp = num_of_pub_dblp
        self.hindex_google_scholar = hindex_google_scholar
        self.num_of_citations_google_scholar = num_of_citations_google_scholar
        self.num_of_pub_scopus = num_of_pub_scopus
        self.hindex_scopus = hindex_scopus

    def empty(self):
        return self.firstname == '' and self.lastname == ''

    def to_string(self):
        return '\n' \
               'Imię: \t\t\t\t\t\t\t\t%s\n' \
               'Nazwisko: \t\t\t\t\t\t\t%s\n' \
               'Tytuł: \t\t\t\t\t\t\t\t%s\n' \
               'Dziedzina: \t\t\t\t\t\t\t%s\n' \
               'Jednostka nadająca tytuł:\t\t\t%s\n' \
               'Aktualne miejsce pracy:\t\t\t\t%s\n' \
               'Liczba cytowań w Google Scholar: \t%s\n' \
               'H-index Google Scholar: \t\t\t%s\n' \
               'Liczba publikacji w DBLP: \t\t\t%s\n' \
               'Liczba publikacji w Scopus: \t\t%s\n' \
               'H-index Scopus: \t\t\t\t\t%s\n' \
               % \
               (self.firstname, self.lastname, self.academic_degree, self.discipline,
                self.home_university, self.work_university,
                self.num_of_citations_google_scholar, self.hindex_google_scholar,
                self.num_of_pub_dblp, self.num_of_pub_scopus, self.hindex_scopus
                )

    def __repr__(self):
        return '%s %s %s %s %s' % (
            self.academic_degree, self.firstname, self.lastname, self.discipline, self.home_university)

    def __str__(self):
        return '%s %s %s %s %s' % (
            self.academic_degree, self.firstname, self.lastname, self.discipline, self.home_university)
