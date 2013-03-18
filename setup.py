# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.about',
    version=version,
    description="The About box for a GroupServer Group",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='group membership group groupserver',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'Zope2',
        'zope.browserresource',
        'zope.cachedescriptors',
        'zope.component',
        'zope.formlib',
        'zope.interface.interface',
        'zope.schema',
        'zope.viewlet',
        'gs.content.form',
        'gs.group.base',
        'gs.group.home',
        'gs.help',
        'gs.viewlet',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)

