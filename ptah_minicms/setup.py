import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'ptah >= 0.5.0',
    'ptahcms >= 0.5.0',
    'ptah_crowd >= 0.2dev',
    'pyramid >= 1.3',
    'pyramid_beaker >= 0.6.1',
    'pyramid_exclog',
    'pyramid_debugtoolbar']

test_requires = [
    'nose',
    'ptah',
    'pyramid',]


setup(name='ptah_minicms',
      version='0.2',
      description='ptah_minicms',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      test_suite = 'nose.collector',
      entry_points = """\
        [paste.app_factory]
        main = ptah_minicms.app:main
      """,
      paster_plugins=['pyramid'],
      )
