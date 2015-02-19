# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2015 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals
from zope.interface.interface import Interface
from zope.schema import Text
from zope.viewlet.interfaces import IViewletManager
from . import GSMessageFactory as _


class IChangeAbout(Interface):
    aboutText = Text(
        title=_('text-entry-label', 'Text'),
        description=_('text-entry-description',
                      'The text that appears in the About tab.'),
        required=False)


class IGroupAboutInfo(IViewletManager):
    '''All the information in the viewlet manager'''
