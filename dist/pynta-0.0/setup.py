# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pynta',
    version='0.0',
    description='Python Nanoparticle Tracking Analysis',
    packages=find_packages(),
    url='https://github.com/nanoepics/pynta',
    license='GPLv3',
    author='Aquiles Carattino',
    author_email='aquiles@aquicarattino.com',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ],
    # package_data={'pynta': ['view/Monitor/Icons/*.*', 'view/Monitor/Icons/*.*']},
    include_package_data=True,
    install_requires=['',]
)
