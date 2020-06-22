from setuptools import setup

setup(
   name='bluecat_edge',
   version='0.1.0',
   author='Scott Penney',
   author_email='spenney@bluecatnetworks.com',
   packages=['bluecat_edge'],
   scripts=['bin/tester.py'],
   url='http://pypi.python.org/pypi/bluecat_edge/',
   license='LICENSE.txt',
   description='Functions to access and interact with a BlueCat Edge CI',
   long_description=open('README.txt').read(),
   install_requires=[
      "requests>=2.23.0",
      "PyYAML>=5.3.1",
      "pytest",
      "dataclasses_json>=0.5.1",
      "marshmallow>=3.6.1", 
      "marshmallow-enum>=1.5.1", 
      "mypy-extensions>=0.4.3", 
      "stringcase>=1.2.0", 
      "typing-extensions>=3.7.4.2", 
      "typing-inspect>=0.6.0",
      "expiringdict>=1.2.1",
   ],
)