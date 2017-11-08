#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sylvain Josserand'
SITENAME = 'Intuitivo - Formations sur Python et Django'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://python.org/'),
    ('Django', 'https://www.djangoproject.com/'),
)
# Social widget
SOCIAL = (('Mon CV sur DoYouBuzz', 'http://sylvain-josserand.fr'),
        ('Twitter', 'https://www.twitter.com/SylvainJoss'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['supports', ]
ARTICLE_PATHS = ['blog', ]
