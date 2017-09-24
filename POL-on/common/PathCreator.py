# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class PathCreator:
    def __init__(self):
        pass

    def create_polon_phd_db_dir_path(self, resource_name=''):
        tmp = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(tmp[0], 'databases', resource_name)
        return path

    def create_polon_phd_db_file_path(self, resource_name=''):
        tmp = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(tmp[0], 'databases', 'phds', resource_name)
        return path

    def create_polon_phd_dir_path(self, resource_name=''):
        tmp = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(tmp[0], 'polon', 'phds', resource_name)
        return path

    def create_polon_phd_file_path(self, resource_name=''):
        tmp = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(tmp[0], 'polon', 'phds', resource_name)
        return path

    def create_itranking_dir_path(self, resource_name=''):
        tmp = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(tmp[0], 'data', 'html_files', resource_name)
        return path

    def create_umcsranking_dir_path(self, resource_name=''):
        tmp = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(tmp[0], 'data', 'html_files_umcs', resource_name)
        return path


if __name__ == "__main__":
    pc = PathCreator()

    print pc.create_polon_phd_dir_path()
    print pc.create_polon_phd_db_dir_path()

    print pc.create_polon_phd_db_file_path('POLon_PhD_All_DB.sql')
    print pc.create_polon_phd_db_file_path('POLon_PhD_IT_DB.sql')
