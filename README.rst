
Requirements
============

The plugin works as expected under Python 2.7 and Python 3.4. The following libraries 
(along with those required by django-cms) are necessary:

- ``Django`` >= 1.5
- ``django-cms`` >= 2.4 (include all of Django CMS 3.x releases)
- ``python-nvd3``


Installation
============

It is assumed that django-cms already installed. Additionally, you need install ``python-nvd3`` module. 
 
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

Create your database (If you working with ``django 1.7`` and higher) ::

  manage.py makemigrations cmsplugin_nvd3
  
  manage.py migrate cmsplugin_nvd3

If your Django version is lower 1.7, use ``syncdb`` command ::

  manage.py syncdb

The plugin can be used in a single manner or embedded into text plugins.


