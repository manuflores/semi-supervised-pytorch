import setuptools 

with open("README.md", "r") as f: 
	long_description = f.read()


setuptools.setup(
	name = 'semisupervised', 
	version = '0.0.1', 
	author = 'Jesper Wohlert and Emanuel Flores', 
	author_email = 'manuflores@caltech.edu', 
	description = 'Implementations of semisupervised learning in PyTorch.', 
	long_description = long_description, 
	long_description_content_type = 'ext/markdown', 
	packages = setuptools.find_packages(),
	classifiers =(
		"Programming Language :: Python :: 3", 
		"Operating System :: OS Independent"
	)
)
