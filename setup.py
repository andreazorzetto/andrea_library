# setup.py

from setuptools import setup, find_packages

setup(
    name='andrea_library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add other dependencies here
    ],
    author='Andrea Zorzetto',
    author_email='andrea@thatpersonalmail.com',
    description='Collection of API calls for Aqua Security',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/andreazorzetto/andrea_library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
