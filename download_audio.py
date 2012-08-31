#!/usr/bin/python
#coding: utf-8
##
##

import time
import mechanize
import cookielib
# import pysox
from bs4 import BeautifulSoup

# Browser
br = mechanize.Browser()

# CookieJar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)

# Want debugging messages?
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

# User Agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Proxy
br.set_proxies({"http":"user:password@123.456.789.101:60099"})

simples_url = ""

som_url = ""

image_url = ""

mp3_filename = ""

filetype = ".mp3"

# for i in xrange(100):
br.open(image_url)
br.retrieve(som_url,mp3_filename+str(0)+filetype)

