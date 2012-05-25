# coding=utf-8
from zope.interface.interface import Interface
from zope.schema import Text

class IChangeAbout(Interface):
    aboutText = Text(title=u'Text',
        description=u'The text that appears in the About tab.',
        required = False)

