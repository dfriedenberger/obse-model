from setuptools import setup
from obse import __version__

setup(name='obse',
      version=__version__,
      description='Library for Ontology Based System Engineering.',
      url='https://github.com/dfriedenberger/obse.git',
      long_description=open('README.md', encoding="UTF-8").read(),
      long_description_content_type='text/markdown',
      author='Dirk Friedenberger',
      author_email='projekte@frittenburger.de',
      license='GPLv3',
      packages=['obse'],
      package_data={'': ['statemachine.ttl']},
      install_requires=[],
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
      ],
      zip_safe=False)
