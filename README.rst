)DVD Fingerprint
===============

This is a Python implementation of the disc fingerprinting technique used by the
Discident_ Database. Works by traversing a directory (from a
DVD drive or ripped) and creating a unique hash for that disc.
 
.. _Discident: http://discident.com/

Usage
-----

Command line::

    $ dvdfingerprint /Volumes/DVD_VIDEO/

From your own code::

    import dvdfingerprint
    dvdfingerprint.fingerprint("/Volumes/DVD_VIDEO/")

Adapted from Erik Kastner's Ruby implementation dvd_fingerprint_.

.. _dvd_fingerprint: https://github.com/kastner/dvd_fingerprint
