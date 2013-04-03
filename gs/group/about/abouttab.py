# -*- coding: utf-8 -*-
from gs.group.base import GroupViewlet


class AboutTab(GroupViewlet):
    pass


class AboutInfo(GroupViewlet):
    @property
    def aboutText(self):
        retval = getattr(self.context, 'aboutText', '')
        return retval
