#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from bs4 import BeautifulSoup

from common.Scientist import Scientist
from polon.POLonParser import POLonParser

reload(sys)
sys.setdefaultencoding("utf8")


class POLonPhDParser(POLonParser):
    def __init__(self):
        POLonParser.__init__(self)

    def parse(self, html):

        soup = BeautifulSoup(html, 'html.parser')

        colcounter = 0
        row = []

        trs = soup.findAll("tr", {"class": "rf-dt-r"})
        for tr in trs:
            tds = tr.findAll("td", {"class": "rf-dt-c"})
            for td in tds:
                row.append(td.text.strip())
                colcounter += 1

            if colcounter == 6:
                colcounter = 0
                self.scientists.append(
                    Scientist(' '.join(row[1].split()[1:]).title(), ' '.join(row[2].split()[1:]).title(), ' '.join(row[3].split()[2:4]),
                              ' '.join(row[4].split()[42:]), ' '.join(row[5].split()[4:])))
                row[:] = []

        return self.scientists


if __name__ == "__main__":
    pass
