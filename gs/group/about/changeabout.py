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
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base.wymeditor import wym_editor_widget
from gs.content.form.base.utils import enforce_schema
from gs.group.base.form import GroupForm
from . import GSMessageFactory as _
from .audit import Auditor, CHANGE_ABOUT
from .interfaces import IChangeAbout


class ChangeAbout(GroupForm):
    label = _('change-form-label', 'Change about')
    pageTemplateFileName = 'browser/templates/changeabout.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, group, request):
        GroupForm.__init__(self, group, request)

    @Lazy
    def form_fields(self):
        enforce_schema(self.context, IChangeAbout)
        retval = form.Fields(IChangeAbout, render_context=True)
        retval['aboutText'].custom_widget = wym_editor_widget
        return retval

    @form.action(name="change", label=_('change-action', 'Change'),
                 failure='handle_change_action_failure')
    def handle_invite(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)

        auditor = Auditor(self.siteInfo, self.groupInfo)
        admin = createObject('groupserver.LoggedInUser', self.context)
        l = '{0}'.format(len(data['aboutText'])) \
            if data['aboutText'] else '0'
        auditor.info(CHANGE_ABOUT, admin, l)

        self.status = _(
            'change-status-success',
            'The About tab on the homepage for '
            '<a href="${groupUrl}">${groupName}</a> has been changed.',
            mapping={'groupUrl': self.groupInfo.relativeURL,
                     'groupName': self.groupInfo.name})

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = _('status-problem', '<p>There is an error:</p>')
        else:
            self.status = _('status-problems', '<p>There are errors:</p>')
