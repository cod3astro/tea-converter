from setuptools import setup, find_packages

setup(
    name='rectangle_area',
    version='1.0.0',
    packages=find_packages(),
    author='Your Name',
    author_email='your@email.com',
    description='A simple package to calculate the area of a rectangle',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/rectangle_area',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
