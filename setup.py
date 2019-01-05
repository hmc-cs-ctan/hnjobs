import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="hnjobs_pkg",
	version="0.0.1",
	author="Charleen Tan",
	author_email="charleentan1113@gmail.com",
	description="A small package that supports searching keywords in Hacker News job posts within a time period",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/hmc-cs-ctan/hnjobs",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)