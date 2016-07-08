from setuptools import setup, find_packages

setup(
    name='plottools',
    version='0.1.1',
    license='GNU GENERAL PUBLIC LICENSE',
	description='Plot functions that come in handy',
	url='',
	author='Brecht Baeten',
	author_email='brecht.baeten@gmail.com',
	packages=find_packages(),
	install_requires=['matplotlib'],
	classifiers = ['Programming Language :: Python :: 2.7'],
)