#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.PathCreator import PathCreator
from database_management.POLonDB_PhD import POLonDB_PhD


class DjangoTemplatesBuilder:

    def __init__(self):
        self.path_creator = PathCreator()

    def build_html(self, phds, type=None):

        i = 1

        html = ""
        html += "<table border=\"1\"> <tbody>"
        html += "<tr align=\"center\">"
        html += "<th>Numer</th>"
        html += "<th>Imię</th>"
        html += "<th>Nazwisko</th>"
        html += "<th>Tytuł</th>"
        html += "<th>Dziedzina</th>"
        html += "<th>Jednostka nadająca tytuł</th>"
        html += "<th>Liczba Cytowań Google Scholar</th>"
        html += "<th>H-Index Google Scholar</th>"
        html += "<th>Liczba Publikacji w DBLP</th>"
        html += "<th>Liczba Publikacji w Scopus</th>"
        html += "<th>H-Index Scopus</th>"
        html += "</tr>"

        for phd in phds:

            if type is not None:
                if type == 'dr':
                    if phd.academic_degree != 'doktor':
                        phd = None
                elif type == 'drhab':
                    if phd.academic_degree != 'doktor habilitowany':
                        phd = None

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

    def build_html_google_scholar_citations(self, dbname, type=None):

        db = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(dbname))
        db.create_table()
        phds = db.select_all_sort_by_google_scholar_citations()


        # create filename
        filename = "google_scholar_citations_"

        if type == 'dr':
            filename = filename + "drhab.html"
        elif type == 'drhab':
            filename = filename + "dr.html"
        else:
            filename = filename + "all.html"

        # create path
        path = self.path_creator.create_itranking_dir_path(filename)

        # create html header
        html_header = "{% extends \"base.html\" %} \n" \
                      "{% block title %}Welcome to Polish IT Ranking Database{% endblock %}\n" \
                      "{% block head %}Researchers Metrics Sorted by the Number of Citations in Google Scholar{% endblock %}\n" \
                      "{% block content %}\n\n"
        # create html footer
        html_footer = "{% endblock %}"

        # build HTML
        html = html_header + self.build_html(phds, type) + "\n\n" + html_footer

        # save to file
        with open(path, 'w') as f:
            f.write(html)

        return html

    def build_html_google_scholar_hindex(self, dbname, type=None):

        db = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(dbname))
        db.create_table()
        phds = db.select_all_sort_by_google_scholar_hindex()

        # create filename
        filename = "google_scholar_hindex_"

        if type == 'dr':
            filename = filename + "drhab.html"
        elif type == 'drhab':
            filename = filename + "dr.html"
        else:
            filename = filename + "all.html"

        # create path
        path = self.path_creator.create_itranking_dir_path(filename)

        # create html header
        html_header = "{% extends \"base.html\" %} \n" \
                      "{% block title %}Welcome to Polish IT Ranking Database{% endblock %} \n" \
                      "{% block head %}Researchers Metrics Sorted by the H-Index in Google Scholar{% endblock %}\n" \
                      "{% block content %}\n\n"
        # create html footer
        html_footer = "{% endblock %}"

        # build HTML
        html = html_header + self.build_html(phds, type) + "\n\n" + html_footer

        # save to file
        with open(path, 'w') as f:
            f.write(html)

        return html

    def build_html_dblp_num_of_pubs(self, dbname, type=None):
        i = 1
        db = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(dbname))
        db.create_table()
        phds = db.select_all_sort_by_dblp_all_num_of_pubs()

        # create filename
        filename = "dblp_num_of_pubs_"

        if type == 'dr':
            filename = filename + "drhab.html"
        elif type == 'drhab':
            filename = filename + "dr.html"
        else:
            filename = filename + "all.html"

        # create path
        path = self.path_creator.create_itranking_dir_path(filename)

        # create html header
        html_header = "{% extends \"base.html\" %} \n" \
                      "{% block title %}Welcome to Polish IT Ranking Database{% endblock %}\n" \
                      "{% block head %}Researchers Metrics Sorted by the Number of Publications in DBLP{% endblock %}\n" \
                      "{% block content %}\n\n"
        # create html footer
        html_footer = "{% endblock %}"

        # build HTML
        html = html_header + self.build_html(phds, type) + "\n\n" + html_footer

        # save to file
        with open(path, 'w') as f:
            f.write(html)

        return html

    def build_html_scopus_hindex(self, dbname, type=None):
        i = 1
        db = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(dbname))
        db.create_table()
        phds = db.select_all_sort_by_scopus_hindex()

        # create filename
        filename = "scopus_hindex_"

        if type == 'dr':
            filename = filename + "drhab.html"
        elif type == 'drhab':
            filename = filename + "dr.html"
        else:
            filename = filename + "all.html"

        # create path
        path = self.path_creator.create_itranking_dir_path(filename)

        # create html header
        html_header = "{% extends \"base.html\" %}\n" \
                      "{% block title %}Welcome to Polish IT Ranking Database{% endblock %}\n" \
                      "{% block head %}Researchers Metrics Sorted by the H-Index Scopus{% endblock %}\n" \
                      "{% block content %}\n\n"
        # create html footer
        html_footer = "{% endblock %}"

        # build HTML
        html = html_header + self.build_html(phds, type) + "\n\n" + html_footer

        # save to file
        with open(path, 'w') as f:
            f.write(html)

        return html

    def build_html_scopus_num_of_pubs(self, dbname, type=None):
        i = 1
        db = POLonDB_PhD(self.path_creator.create_polon_phd_db_file_path(dbname))
        db.create_table()
        phds = db.select_all_sort_by_scopus_all_num_of_pubs()

        # create filename
        filename = "scopus_num_of_pubs_"

        if type == 'dr':
            filename = filename + "dr.html"
        elif type == 'drhab':
            filename = filename + "drhab.html"
        else:
            filename = filename + "all.html"

        # create path
        path = self.path_creator.create_itranking_dir_path(filename)

        # create html header
        html_header = "{% extends \"base.html\" %}\n" \
                      "{% block title %}Welcome to Polish IT Ranking Database{% endblock %}\n" \
                      "{% block head %}Researchers Metrics Sorted by the Number of Publications in Scopus{% endblock %}\n" \
                      "{% block content %}\n\n"
        # create html footer
        html_footer = "{% endblock %}"

        # build HTML
        html = html_header + self.build_html(phds, type) + "\n\n" + html_footer

        # save to file
        with open(path, 'w') as f:
            f.write(html)

        return html