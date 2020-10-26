#!/usr/bin/env python

#
# Site Metadata
#

AUTHOR = 'A.N. Other'
SITENAME = 'Editorial'
SITESUBTITLE = 'A pelican theme'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

#
# Paths and output locations
#

PATH = 'content'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
DIRECT_TEMPLATES = ['search', 'index', 'archives', 'authors', 'categories',
                    'tags', '404']
PAGINATED_TEMPLATES = {'archives': None, 'tag': None, 'category': None, 'author': None}

#
# Plugins
#

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'tipue_search', 'share_post']

#
# Theme
#

THEME = 'theme'


#
# Custom theme elements
#

# Sidebar menu links
#   Entries can be one of:
#     direct-link: (<display text>, <link relative to root>)
#     submenu: (<display text>, (<direct-link>), [<direct-link>]...))

MENUITEMS = (('Homepage', ''),
              ('Generic', 'pages/generic'),
              ('Theme elements', 'elements'),
              ('Pelican pages', (
                  ('Archive', 'archives'),
                  ('Authors', 'authors'),
                  ('Categories', 'categories'),
                  ('Tags', 'tags'))),
              ('You can add entries in your config file', '#'),)

# Contacts at the end of the sidebar
#   Entries are:
#     (<display text>, <link (or None)>, <icon class name>)

CONTACTS = (('information@untitled.tld', '#', 'solid fa-envelope'),
            ('(000) 000-0000', None, 'solid fa-phone'),
            ('1234 Somewhere Road #8254 <br> Nashville, TN 00000-0000',
             None, 'solid fa-home'))

# Social icons in header bar
#   Entries are:
#     (<icon class name>, <link>)

SOCIAL = (('brands fa-github', 'https://github.com/awild82/editorial_pelican'),
          ('brands fa-gitlab', 'https://gitlab.com/awild82/editorial_pelican'),
          ('fa-envelope', '#'))

# Share post options
#  Entries are:
#    (<name>, <share_post_link>, <show>)
#  share_post_link can be one of:
#    facebook, twitter, email, diaspora, linkedin, hacker-news, reddit
SHAREPOST = (('Facebook', 'facebook', True),
             ('Email', 'email', True),
             ('Twitter', 'twitter', True),
             ('Diaspora*', 'diaspora', True),
             ('LinkedIn', 'linkedin', True),
             ('Hacker News', 'hacker-news', True),
             ('Reddit', 'reddit', True))

DEFAULT_PAGINATION = 6
