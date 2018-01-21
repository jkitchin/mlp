# Copyright 2018, John Kitchin
# (see accompanying license files for details).

from setuptools import setup, find_packages

with open('README.org') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
    
setup(name='mlp',
      version='0.0.1',
      description='TODO',
      long_description=readme,
      author='John Kitchin',
      author_email='jkitchin@andrew.cmu.edu',
      url='http://github.com/jkitchin/mlp',
      license=license,
      setup_requires=['nose>=1.0'],
      data_files=['requirements.txt', 'LICENSE'],
      packages=find_packages(exclude=('tests', 'docs')))

# python setup.py register to setup user
# to push to pypi - (shell-command "python setup.py sdist upload")
