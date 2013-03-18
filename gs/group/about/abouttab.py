# coding=utf-8
from gs.group.member.base.viewlet import GroupAdminViewlet


class AboutInfo(GroupAdminViewlet):
    @property
    def aboutText(self):
        return getattr(self.context, 'aboutText', '')


class AboutTab(GroupAdminViewlet):
    pass
