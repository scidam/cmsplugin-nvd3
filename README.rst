
Requirements
============

Plugin works as expected and tested under Python 2.7 and Python 3.4. The following libraries 
(along with those required by django-cms) are required

- ``Django`` >= 1.5
- ``django-cms`` >= 2.4 (include all of Django CMS 3.x releases)
- ``python-nvd3``


Installation
============

It is assumed that django-cms already installed. Additionally, you need install required ``python-nvd3`` module. 
 
::

$ pip install python-nvd3

::

$ pip install cmsplugin-nvd3

Insert plugin app in your ``settings.py`` ::

  INSTALLED_APPS = [
      # ...
      'cmsplugin_nvd3',
  	  #...	
  ]

Create your database (If you working with ``django 1.7`` and higher) ::

  manage.py makemigrations cmsplugin_nvd3
  
  manage.py migrate cmsplugin_nvd3

If your django version is lower 1.7, use ``syncdb`` command ::

  manage.py syncdb

You can use the plugin in a single manner or embed it into text plugins.


