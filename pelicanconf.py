#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hung Le Viet'
SITENAME = 'Hung Le Viet'
SITEURL = 'https://leviethung1280.github.io'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True

SITESUBTITLE = "AI Engineer"
SITEDESCRIPTION = "AI and Technology"
FAVICON = SITEURL + '/images/favicon-16x16.png'
SITELOGO = SITEURL + '/images/avatar.jpeg'


# Add a link to your social media accounts
SOCIAL = (
    ('github', 'https://github.com/ayushkumarshah'),
    ('envelope', 'mailto:ayushkumarshah@gmail.com'),
    ('linkedin','https://np.linkedin.com/in/ayush7'),
    ('twitter','https://twitter.com/ayushkumarshah7'),
    ('facebook','https://www.facebook.com/ayushkumarshah'),
    ('reddit','https://www.reddit.com/user/ayushkumarshah')
)

STATIC_PATHS = ['images', 'extra']
# Main Menu Items
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'))

GOOGLE_ANALYTICS = "UA-1234-5678"
GOOGLE_TAG_MANAGER = "GTM-ABCDEF"

# Code highlighting the theme
PYGMENTS_STYLE = 'friendly'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'



PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME="themes/Flex"
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS= ['assets','sitemap','gravatar','post_stats','feed_summary']


# HOME_HIDE_TAGS = True
FEED_USE_SUMMARY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
