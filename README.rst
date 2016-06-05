About
=====

The plugin provides an easy way to insert non-shophisticated
function graphs to `django-cms`_  driven websites.


More detailed docs with examples are available here_.

.. _here: http://easydan.com/cmsplugin-nvd3-docs/

.. _django-cms: http://django-cms.org/


Requirements
============

The plugin works under Python 2.7+ and Python 3.4+ with all versions of Django supported by Django-CMS. 
The following libraries (along with those required by django-CMS) are required:

- ``Django`` >= 1.5, <=1.9
- ``django-cms`` >= 2.4, <=3.2
- ``python-nvd3`` (tested with 0.14.2)


Installation
============

It is assumed that `django-cms`_ is already installed.
 
::

$ pip install python-nvd3

::

$ pip install cmsplugin-nvd3

Insert the plugin app in your ``settings.py`` ::

  INSTALLED_APPS = [
      # ...
      'cmsplugin_nvd3',
  	  #...	
  ]

Create necessary database tables: ::
 
  manage.py migrate cmsplugin_nvd3


The plugin can be used in a single manner or embedded into text plugins.


Configuration
=============

Behaviour of the plugin is controlled by the following settings (defaults are listed below): ::

    # Value separator for x-data
    CMSNVD3_DATASEP = ','

    # Group separator for y-series
    CMSNVD3_YDATAGROUPSEP = ';'

    # Length of random part of id
    CMSNVD3_ID_RANDOM_LENGTH = 7

    # Container prefix; used only if <container name> field in the model is left empty.
    CMSNVD3_CONT_ID_PREFIX = 'nvd3id_'

    # Default container width;
    CMSNVD3_CONT_WIDTH = 600

    # Default container height;
    CMSNVD3_CONT_HEIGHT = 400

    # Maximum allowed container size; all values of width or height will be
    # reduced to defaults if they exceed this value
    CMSNVD3_MAX_CONT_DIM = 3000

    # D3, NVD3 sources.
    CMSNVD3_D3JS_SOURCE = '//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js'
    CMSNVD3_JS_SOURCE = '//cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.min.js'
    CMSNVD3_CSS = '//cdn.rawgit.com/novus/nvd3/v1.8.1/build/nv.d3.css'
    # If one or all of these constants was set up to 'local' (e.g. CMSNVD3_CSS='local'), 
    # the static resource(s) will be loaded via path CMSNVD3_URL

    #a path for d3, nvd3 static files, defined as: STATIC_URL+CMSNVD3_URL 
    CMSNVD3_URL = 'nvd3plugin/'

    #Floating point delimiter. You probably will never need to change it.
    CMSNVD3_FLT_DELIMITER = '.'

