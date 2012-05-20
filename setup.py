import dvdfingerprint

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='dvdfingerprint',
    description='A DVD Fingerprint Geneator',
    long_description=open('README.rst').read(),
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    url='https://github.com/kolanos/dvdfingerprint',
    version=dvdfingerprint.__version__,
    license='BSD',
    install_requires=[],
    test_suite='',
    packages=['dvdfingerprint'],
    scripts=['bin/dvdfingerprint']
)
