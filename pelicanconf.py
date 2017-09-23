#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Code for Maine administrator'
SITENAME = 'Code for Maine'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
THEME = 'themes/semantic-ui'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Blogroll
LINKS = (("Join us on Slack!", "http://bit.do/civicslack"),
         ('Code for Boston', 'http://codeforboston.org/'),
         ('Code for America', 'http://codeforamerica.org/'),)

# Social widget
SOCIAL = (('code4maine @Github', 'https://github.com/code4maine'),
          ('Twitter', 'https://twitter.com/code4maine'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
