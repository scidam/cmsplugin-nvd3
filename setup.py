import os
from setuptools import setup

README_FILE = 'README.md'


def get_long_description():
    if not os.path.isfile(README_FILE):
        return ''
    try:
        import pypandoc
        doc = open(README_FILE).read()
        description = pypandoc.convert(doc, 'rst', format='markdown')
    except Exception:
        description = open(README_FILE).read()
    return description

setup(name='cmsplugin-nvd3',
      packages=['cmsplugin-nvd3'],
      version='0.1',
      description='Embedding nvd3 charts into django-cms driven sites',
      keywords='django,django-cms,nvd3,plugin,charts',
      long_description=get_long_description(),
      author='Dmitry E. Kislov',
      author_email='kislov@easydan.com',
      url='https://github.com/scidam/cmsplugin-nvd3',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience ::  Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Multimedia :: Graphics :: Presentation'
          ],
      )
