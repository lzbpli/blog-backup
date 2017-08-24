# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'ikerbo'
SITENAME = "码  链"
SITEURL = 'http://ikerbo.info'
TIMEZONE = "Asia/Shanghai"

# can be useful in development, but set to False when you're ready to publish
SITETITLE = '码  链'
SITESUBTITLE = '想写点什么！!'
#GRAVATAR_IMAGE = 'https://ooo.0o0.ooo/2017/03/22/58d2308b67793.png'
RELATIVE_URLS = True
THEME = 'voidy-bootstrap/'

#SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
SITETAG = "想写点什么！!"
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
#CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"
SIDEBAR = "sidebar.html"

GITHUB_URL = 'http://ikerbo.info'
#DISQUS_SITENAME = "blog-notmyidea"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2017, 3, 2, 14, 1, 1)

#FEED_ALL_RSS = 'feeds/all.rss.xml'
#CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Zubin Mithra', "http://zubin71.wordpress.com/"),)

SOCIAL = (('ikerbo', 'http://ikerbo.com'),
          ('github', 'http://github.com/lzbpli'),)

# global metadata to all the contents
DEFAULT_METADATA = {'yeah': 'it is'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    ]

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"