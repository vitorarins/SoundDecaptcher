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
br.set_proxies({"http":"neoway:t7710176392o@216.108.225.190:60099"})

simples_url = "http://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATBHE/ConsultaOptantes.app/ConsultarOpcao.aspx"

som_url = "http://www8.receita.fazenda.gov.br/scripts/srf/intercepta/captcha.aspx?opt=sound"

image_url = "http://www8.receita.fazenda.gov.br/scripts/srf/intercepta/captcha.aspx?opt=image"

mp3_filename = "/home/vitor/Documents/Projetos/Captcha/Sound/Simples/som"

filetype = ".mp3"

# for i in xrange(100):
br.open(image_url)
br.retrieve(som_url,mp3_filename+str(0)+filetype)

