#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.PathCreator import PathCreator
from database_management.POLonDB_PhD import POLonDB_PhD
import sys

reload(sys)
sys.setdefaultencoding("utf-8")



class StatType:
    GOOGLE_SCHOLAR_CITATIONS = 1
    GOOGLE_SCHOLAR_HINDEX = 2
    DBLP_NUM_OF_PUBS = 3
    SCOPUS_HINDEX = 4
    SCOPUS_NUM_OF_PUBS = 5

class HTMLBuilder:

    def __init__(self):
        self.path_creator = PathCreator()

    def build_index_page(self):

        html = "<html>\n" \
               "<header>\n" \
               "<title>UMCS Ranking Database</title>\n" \
               "</header>\n" \
               "<body>\n" \
               "<center><p>Kindly Welcome! Here U can find some metrics collected about UMCS' researchers.</br></br></p></center>\n" \
               \
               "<div align=\"center\">\n" \
               "\t<div align=\"left\">\n" \
               "\t\t<p align=\"left\"><b>All (MSc, PhDs, Professors)</b></p>\n" \
               "\t\t<div align=\"left\">\n" \
               "\t\t\t<ul>\n" \
               "\t\t\t\t<li><a href=\"google_scholar_citations.html\">Researchers Metrics Sorted by the <i>Number of Citations</i> in <b>Google Scholar</b></a></li>\n" \
               "\t\t\t\t<li><a href=\"google_scholar_hindex.html\">Researchers Metrics Sorted by the <i>H-index</i> in <b>Google Scholar</b></a></li>\n" \
               "\t\t\t\t<li><a href=\"dblp_num_of_pubs.html\">Researchers Metrics Sorted by the <i>Number of Publications</i> in <b>DBLP</b></a></li>\n" \
               "\t\t\t\t<li><a href=\"scopus_hindex.html\">Researchers Metrics Sorted by the <i>H-Index</i> in <b>Scopus</b></a></li>\n" \
               "\t\t\t\t<li><a href=\"scopus_num_of_pubs.html\">Researchers Metrics Sorted by the <i>Number of Publications</i> in <b>Scopus</b></a></li><br/>\n" \
               "\t\t\t\t\n" \
               "\t\t\t</ul>\n" \
               "\t\t</div>\n" \
               "\t</div>\n" \
               "</div>\n" \
                \
               "</body>\n"

        path = self.path_creator.create_umcsranking_dir_path('index.html')

        with open(path, 'w') as f:
            f.write(html.encode('utf8'))


        return html

    def build_html(self, phds):

        i = 1

        html = ""
        html += u"<table border=\"1\"> <tbody>"
        html += u"<tr align=\"center\">"
        html += u"<th>Numer</th>"
        html += u"<th>Imie</th>"
        html += u"<th>Nazwisko</th>"
        html += u"<th>Tytul</th>"
        html += u"<th>Dziedzina</th>"
        html += u"<th>Jednostka nadajaca tytuł</th>"
        html += u"<th>Liczba Cytowan Google Scholar</th>"
        html += u"<th>H-Index Google Scholar</th>"
        html += u"<th>Liczba Publikacji w DBLP</th>"
        html += u"<th>Liczba Publikacji w Scopus</th>"
        html += u"<th>H-Index Scopus</th>"
        html += u"</tr>"

        for phd in phds:

            if phd is not None:
                html += "<tr align=\"center\">"

                html += "<td>"
                html += "%s" % i
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.firstname
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.lastname
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.academic_degree
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.discipline
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.home_university
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.num_of_citations_google_scholar
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.hindex_google_scholar
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.num_of_pub_dblp
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.num_of_pub_scopus
                html += "</td>"

                html += "<td>"
                html += "%s" % phd.hindex_scopus
                html += "</td>"

                i += 1

                html += "</tr>"

        html += "</tbody></table>"

        return html


    def get_page_title(self, stattype):

        title = ""

        if stattype == StatType.GOOGLE_SCHOLAR_CITATIONS:
            return "Researchers Metrics Sorted by the Number of Citations in Google Scholar"
        elif stattype == StatType.GOOGLE_SCHOLAR_HINDEX :
            return "Researchers Metrics Sorted by the H-Index in Google Scholar"
        elif stattype == StatType.DBLP_NUM_OF_PUBS:
            return "Researchers Metrics Sorted by the Number of Publications in DBLP"
        elif stattype == StatType.SCOPUS_HINDEX:
            return "Researchers Metrics Sorted by the H-Index Scopus"
        elif stattype == StatType.SCOPUS_NUM_OF_PUBS:
            return "Researchers Metrics Sorted by the Number of Publications in Scopus"
        else:
            return ""

    # def build_web_of_science(self, phds, filename):
    #
    #     i = 1
    #
    #     path = self.path_creator.create_umcsranking_dir_path(filename)
    #
    #     html = ""
    #     html += u"<table border=\"1\"> <tbody>"
    #     html += u"<tr align=\"center\">"
    #     html += u"<th>Numer</th>"
    #     html += u"<th>Imie</th>"
    #     html += u"<th>Nazwisko</th>"
    #     html += u"<th>Tytul</th>"
    #     html += u"<th>Liczba Publikacji w Web of Science</th>"
    #     html += u"<th>Liczba Cytowan w Web of Science</th>"
    #     html += u"</tr>"
    #
    #     for phd in phds:
    #
    #         if phd is not None:
    #             html += "<tr align=\"center\">"
    #
    #             html += "<td>"
    #             html += "%s" % i
    #             html += "</td>"
    #
    #             html += "<td>"
    #             html += "%s" % phd.firstname
    #             html += "</td>"
    #
    #             html += "<td>"
    #             html += "%s" % phd.lastname
    #             html += "</td>"
    #
    #             html += "<td>"
    #             html += "%s" % phd.academic_degree
    #             html += "</td>"
    #
    #             html += "<td>"
    #             html += "%s" % phd.num_of_citations_google_scholar
    #             html += "</td>"
    #
    #             html += "<td>"
    #             html += "%s" % phd.hindex_google_scholar
    #             html += "</td>"
    #
    #             i += 1
    #
    #             html += "</tr>"
    #
    #     html += "</tbody></table>"
    #
    #     with open(path, 'w') as f:
    #         f.write(html.encode('utf8'))
    #
    #     return html

    def build_page(self, page_title, phds, stattype):

        path = self.path_creator.create_umcsranking_dir_path(page_title)

        html = u"<html>\n" \
               u"<header>\n" \
               u"<title>%s</title>\n" \
               u"</header>\n" \
               u"<body>\n" \
               u"<center><p>Kindly Welcome! Here U can find %s</br></br></p></center>\n" \
               u"<div align=\"center\">\n" \
               u"%s" \
               u"</div>\n" \
               u"</body>\n" % (self.get_page_title(stattype), self.get_page_title(stattype), self.build_html(phds))

        with open(path, 'w') as f:
            f.write(html.encode('utf8'))

        return html

if __name__ == "__main__":

    path_creator = PathCreator()

    db = POLonDB_PhD(path_creator.create_polon_phd_db_file_path('POLon_PhD_IT_UMCS_DB.sql'))
    db.create_table()

    builder = HTMLBuilder()
    builder.build_index_page()

    # google scholar
    phds = db.select_all_sort_by_google_scholar_citations()
    builder.build_page('google_scholar_citations.html', phds, StatType.GOOGLE_SCHOLAR_CITATIONS)

    phds = db.select_all_sort_by_google_scholar_hindex()
    builder.build_page('google_scholar_hindex.html', phds, StatType.GOOGLE_SCHOLAR_HINDEX)

    # dblp
    phds = db.select_all_sort_by_dblp_all_num_of_pubs()
    builder.build_page('dblp_num_of_pubs.html', phds, StatType.DBLP_NUM_OF_PUBS)

    #scopus
    phds = db.select_all_sort_by_scopus_all_num_of_pubs()
    builder.build_page('scopus_num_of_pubs.html', phds, StatType.SCOPUS_NUM_OF_PUBS)

    phds = db.select_all_sort_by_scopus_hindex()
    builder.build_page('scopus_hindex.html', phds, StatType.SCOPUS_HINDEX)