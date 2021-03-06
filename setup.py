# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014, 2016 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
import codecs
import os
from setuptools import setup, find_packages
from version import get_version

name = 'gs.group.about'
version = get_version()

with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()
with codecs.open(os.path.join("docs", "HISTORY.rst"),
                 encoding='utf-8') as f:
    long_description += '\n' + f.read()

setup(
    name=name,
    version=version,
    description="The About box for a GroupServer Group",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: German",
        "Natural Language :: Spanish",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='group, group page, about box',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='https://github.com/groupserver/{0}'.format(name),
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['.'.join(name.split('.')[:i])
                        for i in range(1, len(name.split('.')))],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.browserpage',
        'zope.browserresource',
        'zope.cachedescriptors',
        'zope.component',
        'zope.formlib',
        'zope.i18n[compile]',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
        'zope.tal',
        'zope.tales',
        'zope.viewlet',
        'Zope2',
        'gs.content.form.base',
        'gs.content.js.wymeditor[zope]',
        'gs.content.js.more[zope]',
        'gs.content.layout',
        'gs.group.base',
        'gs.group.member.viewlet',
        'gs.group.home',
        'gs.help',
        'gs.viewlet',
        'Products.GSAuditTrail',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
