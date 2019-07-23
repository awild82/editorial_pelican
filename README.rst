#####################
Editorial for Pelican
#####################

This is a Pelican template based on the `Editorial HTML template
<https://html5up.net/editorial>`_ of `HTML5UP <https://html5up.net/>`_.

A demo of this template can be found `here <https://TODO.FAKEURL.NET/>`_.

.. contents:: **Contents**
  :local:


Features
========

- Responsive Design (Desktop, Tablet, Tablet (Portrait), Mobile) 
- Static site search via `tipue_search`
- Pygments
- Recent posts in sidebar 

Nice elements
-------------

Due to the pretty classes that HTML5UP had in their HTML template, this Pelican
template comes with some nice elements, which include:

- Support for multi-column formatting
- Image wrapping on left and right
- Fitting images
- Pretty buttons and pagination

See the `Elements page <https://TODO.FAKEURL.NET/elements>`_ for examples of
the above and more!

.. note::
  
  This template works best with reStructuredText documents. I have yet to
  figure out a "nice" way to apply the classes in the css file to Markdown
  sections.


Installation
============

You can clone this repository directly, then modify the entries in the
:code:`content` directory.

Requirements
------------

This template requires :code:`pelican` and :code:`beautifulsoup4` (for Tipue
Search). The :code:`tipue_search` plugin is required for search functionality,
and the :code:`render_math` plugin is recommended for better looking math.

To install the requirements, simply run::

  pip install -r requirements.txt

As the structure stands now, the plugins directory contains symlinks to the
parent directory of the repo, assuming the :code:`pelican-plugins` repository
was installed there. If this is not the case, the symlinks should be amended,
the plugins can be installed into the :code:`plugins` directory directly, or
you can modify your :code:`pelicanconf.py`.

Installing the template only
----------------------------

If you want to start from scratch, or you want your theme to be in a separate
location from your content, you can copy the :code:`theme` folder to wherever
you need it, then modify your :code:`pelicanconf.py` accordingly.

Customization
=============

Configuration Options
---------------------

The templates use the following variables:

+------------------------+---------------------------------------------------+
| Variable               | Use                                               |
+========================+===================================================+
| :code:`MENUITEMS`      | Configuring the links in the navigation section   |
|                        | of the sidebar.                                   |
+------------------------+---------------------------------------------------+
| :code:`CONTACTS`       | Configuring contact links/info at the bottom of   |
|                        | the sidebar.                                      |
+------------------------+---------------------------------------------------+
| :code:`SOCIAL`         | Configuring the icons and links at the top of the |
|                        | page.                                             |
+------------------------+---------------------------------------------------+

When needed, icon class codes should correspond to the font-awesome class. 

These common variables are highly encouraged to have the following settings

+-----------------------------+---------------------------------------------------------------------------------+
| Variable                    | Recommendation                                                                  |
+=============================+=================================================================================+
| :code:`DEFAULT_PAGINATION`  | Multple of 6                                                                    |
+-----------------------------+---------------------------------------------------------------------------------+
| :code:`DIRECT_TEMPLATES`    | :code:`['search', 'index', 'archives', 'authors', 'categories', 'tags', '404']` |
+-----------------------------+---------------------------------------------------------------------------------+
| :code:`PAGINATED_TEMPLATES` | :code:`{'archives': None, 'tag': None, 'category': None, 'author': None}`       |
+-----------------------------+---------------------------------------------------------------------------------+


Modifying the theme
-------------------

You will definitely want to modify `index.html <theme/templates/index.html>`_
and `sidebar.html <theme/templates/sidebar.html>`_. These contain hard coded
text visible in the top portion of the index and the contacts section of the 
sidebar. Everything else *should* be essentially ready for roll-out, but feel
free to tinker as you please!

License and Attributions
========================

License
-------

This template is licensed under the Apache 2.0 license. See `LICENSE
<LICENSE>`_ for more details.

Attributions
------------

This template draws heavily from the fantastic work of others. The design is
entirely based off of (and modified from) the Editorial template by `HTML5UP
<https://html5up.net/>`_ [License - `CCA 3.0`_]. Search is enabled by the Tipue
Search plugin, created by `Tipue <http://tipue.com/>`_ [License - `MIT`_.
Images are from various artists at `Unsplash <https://unsplash.com/>`_ [License
- `Unsplash License`_]. Fonts are Roboto Slab and Open Sans [License - `Apache 2.0`_],
and icons are provided by Font Awesome. 

.. _CCA 3.0: https://creativecommons.org/licenses/by/3.0/legalcode
.. _MIT: https://opensource.org/licenses/MIT
.. _Unsplash License: https://unsplash.com/license
.. _Apache 2.0: http://www.apache.org/licenses/LICENSE-2.0.txt
