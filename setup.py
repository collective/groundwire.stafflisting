from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='groundwire.stafflisting',
      version=version,
      description="Content type and templates to display staff/board listings",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Groundwire',
      author_email='jonb@groundwire.org',
      url='http://groundwire.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['groundwire'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'collective.autopermission',
          'plone.namedfile[blobs]',
          'plone.formwidget.namedfile',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
