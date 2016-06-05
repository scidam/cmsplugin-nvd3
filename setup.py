import os
from setuptools import setup

README_FILE = 'README.rst'

setup(name='cmsplugin-nvd3',
      packages=['cmsplugin_nvd3'],
      version='0.5.2',
      description='Insert nvd3 charts into django-cms driven websites',
      keywords='nvd3,plugin,charts,nvd3-charts,django,django-cms',
      long_description=open(README_FILE).read(),
      include_package_data=True,
      author='Dmitry E. Kislov',
      author_email='kislov@easydan.com',
      url='https://github.com/scidam/cmsplugin-nvd3',
      install_requires=[
          'python-nvd3<=0.14.2',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.4',
          'Framework :: Django :: 1.5',
          'Framework :: Django :: 1.6',
          'Framework :: Django :: 1.7',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.9',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Multimedia :: Graphics :: Presentation'
          ],
      )
