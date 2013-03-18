# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.wymeditor import wym_editor_widget
from gs.content.form.utils import enforce_schema
from gs.group.base.form import GroupForm
from audit import Auditor, CHANGE_ABOUT
from interfaces import IChangeAbout


class ChangeAbout(GroupForm):
    label = u'Change About'
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

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_invite(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)

        auditor = Auditor(self.siteInfo, self.groupInfo)
        admin = createObject('groupserver.LoggedInUser', self.context)
        l = '{0}'.format(len(data['aboutText'])) if data['aboutText'] else '0'
        auditor.info(CHANGE_ABOUT, admin, l)

        s = u'The About tab on the homepage for <a href="{0}/">{1}</a> has '\
            u'been changed.'
        self.status = s.format(self.groupInfo.relativeURL, self.groupInfo.name)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
