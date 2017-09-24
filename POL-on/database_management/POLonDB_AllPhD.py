#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import sqlite3 as sqlite
from common.PathCreator import PathCreator

from common.Scientist import Scientist
from database_management.POLonDB import POLonDB

reload(sys)
sys.setdefaultencoding("utf8")


class POLonDB_AllPhD(POLonDB):
    def __init__(self, dbname):
        POLonDB.__init__(self, dbname)

    ###################################################################################################################################

    def create_table(self):
        sql = '''\
                    CREATE TABLE IF NOT EXISTS POLonAllPhD (
                        ID INTEGER PRIMARY KEY NOT NULL,
                        FIRSTNAME TEXT,
                        LASTNAME TEXT,
                        ACADEMIC_DEGREE TEXT,
                        DISCIPLINE TEXT,
                        HOME_UNI TEXT,
                        WORK_UNI TEXT,
                        NUM_OF_PUB_DBLP INTEGER,
                        HINDEX_GOOGLE_SCHOLAR INTEGER,
                        NUM_OF_CITATIONS_GOOGLE_SCHOLAR INTEGER,
                        NUM_OF_PUB_SCOPUS INTEGER,
                        HINDEX_SCOPUS INTEGER)
                '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

    ###################################################################################################################################

    def insert(self, phd):
        sql = ''' \
                INSERT INTO POLonAllPhD (
                    FIRSTNAME,
                    LASTNAME,
                    ACADEMIC_DEGREE,
                    DISCIPLINE,
                    HOME_UNI,
                    WORK_UNI,
                    NUM_OF_PUB_DBLP,
                    HINDEX_GOOGLE_SCHOLAR,
                    NUM_OF_CITATIONS_GOOGLE_SCHOLAR,
                    NUM_OF_PUB_SCOPUS,
                    HINDEX_SCOPUS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql, (phd.firstname, phd.lastname, phd.academic_degree,
                                         phd.discipline, phd.home_university,
                                         phd.work_university, phd.num_of_pub_dblp,
                                         phd.hindex_google_scholar, phd.num_of_citations_google_scholar,
                                         phd.num_of_pub_scopus, phd.hindex_scopus))
                except sqlite.DatabaseError, dbe:
                    print 'POLonDB_AllPhD::insert ', dbe
        finally:
            connection.close()

    ###################################################################################################################################

    def select_all(self):
        phds = []

        sql = ''' \
                SELECT FIRSTNAME,
                    LASTNAME,
                    ACADEMIC_DEGREE,
                    DISCIPLINE,
                    HOME_UNI,
                    WORK_UNI,
                    NUM_OF_PUB_DBLP,
                    HINDEX_GOOGLE_SCHOLAR,
                    NUM_OF_CITATIONS_GOOGLE_SCHOLAR,
                    NUM_OF_PUB_SCOPUS,
                    HINDEX_SCOPUS FROM POLonAllPhD;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_by_discipline(self, discipline):
        phds = []

        sql = ''' \
                SELECT FIRSTNAME,
                    LASTNAME,
                    ACADEMIC_DEGREE,
                    DISCIPLINE,
                    HOME_UNI,
                    WORK_UNI,
                    NUM_OF_PUB_DBLP,
                    HINDEX_GOOGLE_SCHOLAR,
                    NUM_OF_CITATIONS_GOOGLE_SCHOLAR,
                    NUM_OF_PUB_SCOPUS,
                    HINDEX_SCOPUS
                    FROM POLonAllPhD
                    WHERE DISCIPLINE LIKE ?;
              '''

        format = '%'
        format = format + discipline + format

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql, (format,))
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_by_name(self, firstname, lastname):

        scientist = Scientist()

        format = '%'
        firstname = format + firstname + format

        sql = '''
                SELECT FIRSTNAME,
                LASTNAME,
                ACADEMIC_DEGREE,
                DISCIPLINE,
                HOME_UNI,
                WORK_UNI,
                NUM_OF_PUB_DBLP,
                HINDEX_GOOGLE_SCHOLAR,
                NUM_OF_CITATIONS_GOOGLE_SCHOLAR,
                NUM_OF_PUB_SCOPUS,
                HINDEX_SCOPUS
                FROM
                POLonAllPhD
                WHERE
                FIRSTNAME LIKE ? AND LASTNAME=?;
              '''

        connection = sqlite.connect(self.dbname)
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(sql, (firstname, lastname))
                row = cursor.fetchone()
                if row is not None:
                    scientist = Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        except Exception, e:
            print e
        finally:
            connection.close()
            return scientist

        ###################################################################################################################################


if __name__ == "__main__":
    pc = PathCreator()

    dbname = pc.create_polon_phd_db_file_path('POLon_PhD_All_DB.sql')
    dball = POLonDB_AllPhD(dbname)
    dball.create_table()

    researcher = dball.select_by_name('Bogdan', 'Ksiezopolski')
    print researcher.to_string()
