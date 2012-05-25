# coding=utf-8
from gs.group.home.admin import AdminTab

class AboutInfo(AdminTab):
    @property
    def aboutText(self):
        return getattr(self.context, 'aboutText', '')

class AboutTab(AdminTab):
    pass

