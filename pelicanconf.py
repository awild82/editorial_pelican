#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'A.N. Other'
SITENAME = 'Editorial'
SITESUBTITLE = 'A pelican theme'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'tipue_search']

THEME = 'theme'
DIRECT_TEMPLATES = ['search', 'index', 'archives', 'authors', 'categories',
                    'tags', '404']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sidebar links
MENU_LINKS = (('Homepage', ''),
              ('Generic', 'pages/generic'),
              ('Theme elements', 'elements'),
              ('Pelican pages', (
                  ('Archive', 'archives'),
                  ('Authors', 'authors'),
                  ('Categories', 'categories'),
                  ('Tags', 'tags'))),
              ('You can add entries in your config file', '#'),)

CONTACTS = (('information@untitled.tld', '#', 'solid fa-envelope'),
            ('(000) 000-0000', None, 'solid fa-phone'),
            ('1234 Somewhere Road #8254 <br> Nashville, TN 00000-0000',
             None, 'solid fa-home'))

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('brands fa-github', '#'),
          ('brands fa-gitlab', '#'),
          ('fa-envelope', '#'))

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
