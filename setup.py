# Copyright 2015, John Kitchin
# (see accompanying license files for details).
from setuptools import setup

setup(name='mlp',
      version='0.01',
      description='python computations in science and engineering',
      url='http://github.com/jkitchin/mlp',
      maintainer='John Kitchin',
      maintainer_email='jkitchin@andrew.cmu.edu',
      license='GPL',
      platforms=['linux'],
      packages=['mlp'],
      setup_requires=['nose>=1.0'],
      data_files=['requirements.txt', 'LICENSE'],
      long_description='''TODO''')

# python setup.py register to setup user
# to push to pypi - (shell-command "python setup.py sdist upload")
