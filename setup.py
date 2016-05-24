#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    author='luodaihong',
    author_email='804895134@qq.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description='CAS 1.0/2.0 authentication backend for Django',
    download_url='https://github.com/luodaihong/django_cas.git',
    keywords='django cas cas2 authentication middleware backend',
    license='MIT',
    long_description="""
``django_cas`` is a `CAS`_ 1.0 and CAS 2.0 authentication backend for
`Django`_. It allows you to use Django's built-in authentication mechanisms
and ``User`` model while adding support for CAS.

It also includes a middleware that intercepts calls to the original login and
logout pages and forwards them to the CASified versions, and adds CAS support
to the admin interface.

.. _CAS: http://www.ja-sig.org/products/cas/
.. _Django: http://www.djangoproject.com/
""",
    name='django_cas',
    packages=['django_cas']
    version='2.0.3Luo',
)
