#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Toby Searle'
SITENAME = u'Toby Searle'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('github', 'https://github.com/twsearle'),
          ('linkedin', 'http://linkedin.com'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

HEADER_IMAGE = "header_image_viridis.png"

# This thing moves the blog index off the frontpage and into this html file
INDEX_SAVE_AS = 'blog_index.html'

THEME = "notmyidea"

# Even if you opt to clear the output directory everytime you build, this makes
# sure we don't loose version control
OUTPUT_RETENTION = [".git"]

# Not sure exactly how to use this, just in case the dates look odd
DEFAULT_DATE_FORMAT = '%a %d %B %Y'

# The default for the date, set to fs for filesystem date 
DEFAULT_DATE = 'fs'

GITHUB_URL='https://github.com/twsearle'

# Get pelican to handle the CNAME file
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
