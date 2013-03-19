# coding=utf-8
from gs.group.member.viewlet import GroupAdminViewlet


class AboutInfo(GroupAdminViewlet):
    @property
    def aboutText(self):
        return getattr(self.context, 'aboutText', '')


class AboutTab(GroupAdminViewlet):
    pass
