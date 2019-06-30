# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='vasuki',
      version='0.2.0',
      description='Vasuki generates different kinds of random unique identifiers, tokens and words',
      long_description=README,
      license="AGPL 3, EUPL 1.2",
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "Topic :: Communications",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: System :: Archiving",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Utilities",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
      author='Andreas Motl',
      author_email='andreas@terkin.org',
      url='https://github.com/daq-tools/vasuki',
      keywords='id generator uuid ulid hashid',
      packages=find_packages(),
      include_package_data=True,
      package_data={
      },
      zip_safe=False,
      test_suite='vasuki.test',
      install_requires=[
          'docopt==0.6.2',
          'munch==2.3.2',
          'ulid-py==0.0.9',
          'hashids==1.2.0',
          'gibberish==0.3',
          #'correct-horse==0.3.0',
          #'flufl.i18n==1.1.3',
      ],
      extras_require={
          'service': [
              'responder==1.3.1',
          ],
      },
      dependency_links=[
          'https://github.com/greghaskins/gibberish/tarball/3ec39861#egg=gibberish-0.3',
      ],
      entry_points={
          'console_scripts': [
              'vasuki = vasuki.cli:run',
          ],
      },
)
