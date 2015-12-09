#!/usr/bin/env python3
from setuptools import setup

setup(name='conoha-cli',
      version='0.0.2',
      description='conoha-cli is a command and Python3 library for ConoHa API.',
      url='https://github.com/yuuki0xff/conoha-cli',
      author='yuuki0xff',
      author_email='yuuki0xff@gmail.com',
      license='MIT',
      packages=['conoha'],
      zip_safe=False,
      entry_points={
		  'console_scripts': [
			  'conoha-cli = conoha.cli:main',
		  	  ],
      	  },
      )
