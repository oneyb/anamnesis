#!/usr/bin/env python3
#

DESCRIPTION = 'Simple clipboard manager'
LONG_DESCRIPTION = """\
    See README, please.
"""

DISTNAME = 'anamnesis'
MAINTAINER = 'Brian J. Oney'
MAINTAINER_EMAIL = 'brian.j.oney@gmail.com'
URL = 'https://github.com/oneyb/anamnesis'
LICENSE = 'GPLv3'
DOWNLOAD_URL = 'https://github.com/oneyb/anamnesis'
VERSION = '1.5'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


def check_dependencies():
    install_requires = []
    try:
        import gi, gtk, gobject
    except ImportError:
        print('Install dependencies please')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()
    # install_requires = []

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          entry_points = {
              'console_scripts': [
                  'anamnesis=anamnesis:main',
                  'anamnesis-browser=browser:main',
                  'anamnesis-daemon=anamnesis:restart',
              ],
          },
          packages=['anamnesis'],
          classifiers=[
              'Intended Audience :: Programmers',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: 3.8',
              'License :: OSI Approved :: GPLv3 License',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
    )
