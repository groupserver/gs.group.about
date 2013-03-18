# -*- coding: utf-8 -*-
from pytz import UTC
from datetime import datetime
from zope.component.interfaces import IFactory
from zope.interface import implements, implementedBy
from Products.CustomUserFolder.userinfo import userInfo_to_anchor
from Products.GSGroup.groupInfo import groupInfo_to_anchor
from Products.GSAuditTrail import IAuditEvent, BasicAuditEvent, \
    AuditQuery, event_id_from_data
from Products.XWFCore.XWFUtils import munge_date

SUBSYSTEM = 'gs.group.about'
import logging
log = logging.getLogger(SUBSYSTEM)

UNKNOWN = '0'
CHANGE_ABOUT = '1'


class AuditEventFactory(object):
    implements(IFactory)

    title = u'Group Homepage Audit-Event Factory'
    description = u'Creates a GroupServer audit event for group homepage events'

    def __call__(self, context, event_id, code, date,
        userInfo, instanceUserInfo, siteInfo, groupInfo,
        instanceDatum='', supplementaryDatum='', subsystem=''):
        if code == CHANGE_ABOUT:
            event = ChangeAboutEvent(context, event_id, date, userInfo,
                                    siteInfo, groupInfo, instanceDatum)
        else:
            event = BasicAuditEvent(context, event_id, UNKNOWN, date,
              userInfo, instanceUserInfo, siteInfo, groupInfo,
              instanceDatum, supplementaryDatum, SUBSYSTEM)
        assert event
        return event

    def getInterfaces(self):
        return implementedBy(BasicAuditEvent)


class ChangeAboutEvent(BasicAuditEvent):
    ''' An audit-trail event representing a person changing the About
    tab.'''
    implements(IAuditEvent)

    def __init__(self, context, id, d, adminInfo, siteInfo, groupInfo,
                nchars):
        BasicAuditEvent.__init__(self, context, id, CHANGE_ABOUT, d,
            adminInfo, None, siteInfo, groupInfo, nchars, None,
            SUBSYSTEM)

    def __str__(self):
        retval = u'%s (%s) changed the About text for %s (%s) on '\
            u'%s (%s). It is now %s characters long.' %\
           (self.userInfo.name, self.userInfo.id,
            self.groupInfo.name, self.groupInfo.id,
            self.siteInfo.name, self.siteInfo.id,
            self.instanceDatum,)
        retval = retval.encode('ascii', 'ignore')
        return retval

    @property
    def xhtml(self):
        cssClass = u'audit-event groupserver-group-home-%s' %\
          self.code
        retval = u'<span class="%s">%s changed the About tab on the'\
            u'homepage of %s</span>' % \
                    (cssClass, userInfo_to_anchor(self.instanceUserInfo),
                        groupInfo_to_anchor(self.groupInfo))
        retval = u'%s (%s)' % \
          (retval, munge_date(self.context, self.date))
        return retval


class Auditor(object):
    def __init__(self, siteInfo, groupInfo):
        self.siteInfo = siteInfo
        self.groupInfo = groupInfo

        self.queries = AuditQuery()
        self.factory = AuditEventFactory()

    def info(self, code, adminInfo, instanceDatum='', supplementaryDatum=''):
        d = datetime.now(UTC)
        eventId = event_id_from_data(adminInfo, adminInfo,
            self.siteInfo, code, instanceDatum, supplementaryDatum)

        e = self.factory(self.groupInfo.groupObj, eventId, code, d,
                adminInfo, None, self.siteInfo, self.groupInfo,
                instanceDatum, supplementaryDatum, SUBSYSTEM)

        self.queries.store(e)
        log.info(e)
