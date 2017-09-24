# !/usr/bin/env python
# -*- coding: utf-8 -*-

# SCOPUS_API_KEY = "521c8f455bccbdcee6eb036f9594dc1a"

SCOPUS_API_KEY = "def2a8aa2b91e77547ecef7299843c9b"

# http://api.elsevier.com/documentation/search/AUTHORSearchTips.htm
SCOPUS_SUBJECT_AREAS = {}
SCOPUS_SUBJECT_AREAS['Agricultural and Biological Sciences'] = 'AGRI'
SCOPUS_SUBJECT_AREAS['Arts and Humanities'] = 'ARTS'
SCOPUS_SUBJECT_AREAS['Biochemistry, Genetics and Molecular Biology'] = 'BIOC'
SCOPUS_SUBJECT_AREAS['Business, Management and Accounting'] = 'BUSI'
SCOPUS_SUBJECT_AREAS['Chemical Engineering'] = 'CENG'
SCOPUS_SUBJECT_AREAS['Chemistry'] = 'CHEM'
SCOPUS_SUBJECT_AREAS['Computer Science'] = 'COMP'
SCOPUS_SUBJECT_AREAS['Decision Sciences'] = 'DECI'
SCOPUS_SUBJECT_AREAS['Dentistry'] = 'DENT'
SCOPUS_SUBJECT_AREAS['Earth and Planetary Sciences'] = 'EART'
SCOPUS_SUBJECT_AREAS['Economics, Econometrics and Finance'] = 'ECON'


def available_scopus_subject_areas():
    return SCOPUS_SUBJECT_AREAS.keys()


if __name__ == "__main__":
    scopus_sub_ares = available_scopus_subject_areas()
    print scopus_sub_ares
