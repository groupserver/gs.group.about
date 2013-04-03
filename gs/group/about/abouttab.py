# -*- coding: utf-8 -*-
from gs.group.viewlet import GroupViewlet


class AboutTab(GroupViewlet):
    pass


class AboutInfo(GroupViewlet):
    @property
    def aboutText(self):
        retval = getattr(self.context, 'aboutText', '')
        return retval
