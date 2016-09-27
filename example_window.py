#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys

from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from markdown import markdown


app = QApplication(sys.argv)

md = open(sys.argv[1]).read()

html = markdown(md)

browser = QWebView()
browser.setHtml(html)
#browser.load(QUrl(sys.argv[1]))
browser.show()

app.exec_()
