# coding=utf-8
from zope.formlib import form
from zope.component import createObject
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.wymeditor import wym_editor_widget
from gs.content.form.utils import enforce_schema
from gs.group.base.form import GroupForm
from gs.group.home.audit import Auditor, CHANGE_ABOUT
from interfaces import IChangeAbout

class ChangeAbout(GroupForm):
    label = u'Change the Homepage About Tab'
    pageTemplateFileName = 'browser/templates/changeabout.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, group, request):
        GroupForm.__init__(self, group, request)
        self.__formFields = None
        
    @property
    def form_fields(self):
        if self.__formFields == None:
            enforce_schema(self.context, IChangeAbout)
            self.__formFields = form.Fields(IChangeAbout,  
                                            render_context=True)
            self.__formFields['aboutText'].custom_widget = \
                wym_editor_widget
        return self.__formFields        

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_invite(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)
        
        auditor = Auditor(self.siteInfo, self.groupInfo)
        admin = createObject('groupserver.LoggedInUser', self.context)
        auditor.info(CHANGE_ABOUT, admin, '%d' % len(data['aboutText']))
        
        self.status = u'The About tab on the homepage for '\
          u'<a href="%s">%s</a> has been changed.' %\
          (self.groupInfo.relative_url(), self.groupInfo.name)
        
    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'

