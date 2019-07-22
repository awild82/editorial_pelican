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
PAGINATED_DIRECT_TEMPLATES = ['archives']

#
# Plugins
#

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'tipue_search']

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
#   See README.md for more details

MENU_LINKS = (('Homepage', ''),
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

SOCIAL = (('brands fa-github', '#'),
          ('brands fa-gitlab', '#'),
          ('fa-envelope', '#'))

DEFAULT_PAGINATION = 6
