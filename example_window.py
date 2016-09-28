#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys

from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from markdown import markdown
import urllib2

# Qt4 app
app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle('MDBrowser')




# open url
opener = urllib2.build_opener()
req=urllib2.Request("http://pantoff0l.nl:8080", data=None, headers={'Content-Type': 'text/markdown'})
response = opener.open(req)
md=response.read()

# parse markdown
html = markdown(md)

# add stylesheet
html += "<link href='https://gist.githubusercontent.com/tuzz/3331384/raw/d1771755a3e26b039bff217d510ee558a8a1e47d/github.css' rel='stylesheet' type='text/css'>"

# render markdown
browser = QWebView()
browser.setHtml(html)
#browser.load(QUrl(sys.argv[1]))
browser.show()

app.exec_()
