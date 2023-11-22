# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='vasuki',
      version='0.7.0',
      description='Vasuki generates different kinds of random unique identifiers, tokens, and words',
      long_description=README,
      license="MIT",
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
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
      keywords='random unique identifier token word generator id uuid ulid hashid gibberish nagamani19',
      packages=find_packages(),
      include_package_data=True,
      package_data={
      },
      zip_safe=False,
      test_suite='vasuki.test',
      install_requires=[
          'docopt<1',
          'munch<5',
          'ulid-py<1.2',
          'hashids<1.4',
          'gibberish<0.5',
          #'correct-horse==0.7.0',
          #'flufl.i18n==1.1.3',
      ],
      extras_require={
          'develop': [
              'build<2',
              'bump2version==1.0.1',
              'poethepoet<0.25',
              'twine<5',
          ],
          'service': [
              'responder @ git+https://github.com/kennethreitz/responder.git@12a9b8a471',
              'typesystem<0.3',
          ],
          'test': [
              'pytest<8',
              'pytest-cov<5',
          ],
      },
      entry_points={
          'console_scripts': [
              'vasuki = vasuki.cli:run',
          ],
      },
)
