try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='dvdfingerprint',
    description='DVD Fingerprint',
    author='Michael Lavers',
    author_email='kolanos@gmail.com',
    url='https://github.com/kolanos/dvdfingerprint',
    version='0.1.0',
    license='BSD',
    install_requires=[],
    test_suite='',
    packages=['dvdfingerprint'],
    scripts=['bin/dvdfingerprint']
)
