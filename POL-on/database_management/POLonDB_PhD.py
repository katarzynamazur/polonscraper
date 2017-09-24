#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sqlite3 as sqlite

from common.PathCreator import PathCreator
from common.Scientist import Scientist
from database_management.POLonDB import POLonDB

reload(sys)
sys.setdefaultencoding("utf8")


class POLonDB_PhD(POLonDB):
    def __init__(self, dbname):
        POLonDB.__init__(self, dbname)

    ###################################################################################################################################

    def create_table(self):

        sql = '''
                    CREATE TABLE IF NOT EXISTS ''' + str(self.dbname.split('.')[0].split("/")[-1]) + ''' (
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
        sql = '''
                INSERT INTO ''' + str(self.dbname.split('.')[0].split("/")[-1]) + ''' (
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
                    if phd is not None:
                        cursor.execute(sql, (phd.firstname, phd.lastname, phd.academic_degree,
                                             phd.discipline, phd.home_university,
                                             phd.work_university, phd.num_of_pub_dblp,
                                             phd.hindex_google_scholar, phd.num_of_citations_google_scholar,
                                             phd.num_of_pub_scopus, phd.hindex_scopus))
                except sqlite.DatabaseError, dbe:
                    print 'POLonDB_PhD::insert ', dbe
                except Exception, e:
                    print 'POLonDB_PhD::insert ', e
        finally:
            connection.close()

    ###################################################################################################################################

    def select_all(self):
        phds = []

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
                    ''' + str(self.dbname.split('.')[0].split("/")[-1]) + ''';
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(
                            Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_all_sort_by_dblp_all_num_of_pubs(self):
        phds = []

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
                    ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                    ORDER BY
                    NUM_OF_PUB_DBLP DESC;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(
                            Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_all_sort_by_google_scholar_citations(self):
        phds = []

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
                    ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                    ORDER BY
                    NUM_OF_CITATIONS_GOOGLE_SCHOLAR DESC;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(
                            Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_all_sort_by_google_scholar_hindex(self):
        phds = []

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
                    ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                    ORDER BY
                    HINDEX_GOOGLE_SCHOLAR DESC;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(
                            Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_all_sort_by_scopus_hindex(self):
        phds = []

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
                    ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                    ORDER BY
                    HINDEX_SCOPUS DESC;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(
                            Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_all_sort_by_scopus_all_num_of_pubs(self):
        phds = []

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
                    ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                    ORDER BY
                    NUM_OF_PUB_SCOPUS DESC;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        phds.append(
                            Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10]))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

        return phds

    def select_by_name(self, fistname, lastname):

        scientist = None

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
                ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                WHERE
                FIRSTNAME=? AND LASTNAME=?;
              '''

        connection = sqlite.connect(self.dbname)
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(sql, (fistname, lastname))
                row = cursor.fetchone()
                scientist = Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10])
        except Exception, e:
            print e
            return None
        finally:
            connection.close()

        return scientist

    def select_by_academic_degree(self, degree):
        phds = []

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
                ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                WHERE
                ACADEMIC_DEGREE LIKE ?;
              '''

        connection = sqlite.connect(self.dbname)
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(sql, (degree,))
                rows = cursor.fetchall()
                for row in rows:
                    phds.append(
                        Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                  row[10]))
        finally:
            connection.close()

        return phds

    def select_by_id(self, ID):

        ID = str(ID)
        scientist = None

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
                ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                WHERE
                ID=?;
              '''

        connection = sqlite.connect(self.dbname)
        try:
            with connection:
                cursor = connection.cursor()
                cursor.execute(sql, (ID,))
                row = cursor.fetchone()
                scientist = Scientist(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10])
        finally:
            connection.close()

        return scientist

    ###################################################################################################################################

    def update_google_scholar(self, phd, citations, hindex):

        citations = str(citations)
        hindex = str(hindex)

        sql = '''
                UPDATE ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                SET HINDEX_GOOGLE_SCHOLAR=?,
                NUM_OF_CITATIONS_GOOGLE_SCHOLAR=?
                WHERE
                FIRSTNAME=? AND
                LASTNAME=? AND
                ACADEMIC_DEGREE=? AND
                HOME_UNI=?;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql, (
                        hindex, citations, phd.firstname, phd.lastname, phd.academic_degree, phd.home_university))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

    def update_dblp_num_of_all_pubs(self, phd, dblp_num_of_all_pubs):

        dblp_num_of_all_pubs = str(dblp_num_of_all_pubs)

        sql = '''
                UPDATE ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                SET NUM_OF_PUB_DBLP=?
                WHERE
                FIRSTNAME=? AND
                LASTNAME=? AND
                ACADEMIC_DEGREE=? AND
                HOME_UNI=?;
              '''
        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql, (
                        dblp_num_of_all_pubs, phd.firstname, phd.lastname, phd.academic_degree, phd.home_university))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

    def update_scopus(self, phd, num_of_all_pubs, hindex):
        num_of_all_pubs = str(num_of_all_pubs)
        hindex = str(hindex)

        sql = '''
                UPDATE ''' + str(self.dbname.split('.')[0].split("/")[-1]) + '''
                SET NUM_OF_PUB_SCOPUS=?,
                HINDEX_SCOPUS=?
                WHERE
                FIRSTNAME=? AND
                LASTNAME=? AND
                ACADEMIC_DEGREE=? AND
                HOME_UNI=?;
              '''

        connection = sqlite.connect(self.dbname, check_same_thread=False)
        try:
            with connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql, (
                        num_of_all_pubs, hindex, phd.firstname, phd.lastname, phd.academic_degree, phd.home_university))
                except sqlite.DatabaseError, dbe:
                    print dbe
        finally:
            connection.close()

    ###################################################################################################################################

    def get_number_of_all_phds(self):
        return len(self.select_all())

        ###################################################################################################################################


if __name__ == "__main__":
    pc = PathCreator()
    dbname = pc.create_polon_phd_db_file_path('POLon_PhD_IT_UMCS_DB.sql')

    db = POLonDB_PhD(dbname)
    db.create_table()

    phd = db.select_by_name('Bogdan', 'Ksiezopolski')
    print phd.to_string()

    # i = 1
    # phds = db.select_all_sort_by_dblp_all_num_of_pubs()
    # for phd in phds :
    #     print i, phd.to_string()
    #     i += 1

    # i = 1
    # phds = db.select_all_sort_by_google_scholar_citations()
    # for phd in phds:
    #    print i, phd.to_string()
    #    i += 1
