import setuptools
from setuptools import setup, find_packages


readme = open('README.md').read()
requires = [
	"spotinst_sdk",
	"terminaltables",
        "pyyaml<5"
	]
	

setup(
	name="elasticgroup-cli",
	version="0.5",
	description="CLI for Spotinst Elasticgroups",
	long_description=readme,
	url="https://github.com/amelbakry/elasticgroup-cli",
	author="Ahmed ElBakry",
	author_email="eng.ahmed.elbakry@gmail.com",
	classifiers=[
        	 "Intended Audience :: Developers",
        	 "Intended Audience :: System Administrators",
		 "Programming Language :: Python :: 3",
         	 "Programming Language :: Python :: 3.5",
		 "License :: OSI Approved :: MIT License",
		 "Operating System :: OS Independent",
	 ],
	keywords="spotinst elasticgroup spot aws",
        install_requires = requires,
        data_files=[
          ('/usr/local/bin/', ['./elasticgroup-cli'])
          ]
 )
