# coding=utf-8
from zope.interface.interface import Interface
from zope.schema import Text
from zope.viewlet.interfaces import IViewletManager

class IChangeAbout(Interface):
    aboutText = Text(title=u'Text',
        description=u'The text that appears in the About tab.',
        required = False)

class IGroupAboutInfo(IViewletManager):
    '''All the information in the viewlet manager'''

