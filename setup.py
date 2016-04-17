import os
from setuptools import setup

README_FILE = 'README.rst'

setup(name='cmsplugin-nvd3',
      packages=['cmsplugin_nvd3'],
      version='0.5.1',
      description='Insert nvd3 charts into django-cms driven sites',
      keywords='nvd3,plugin,charts,nvd3-charts,django,django-cms',
      long_description=open(README_FILE).read(),
      include_package_data=True,
      author='Dmitry E. Kislov',
      author_email='kislov@easydan.com',
      url='https://github.com/scidam/cmsplugin-nvd3',
      install_requires=[
          'python-nvd3<=0.14.0',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Multimedia :: Graphics :: Presentation'
          ],
      )
