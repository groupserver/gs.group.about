Introduction
============

The *About* tab on the *Group* page provides some general information
about the group. This product supplies two things `the tab`_ itself,
and `the change page`_ that allows the contents of the tab to be
altered.

The Tab
=======

The tab itself is a viewlet as part of the *Info Tabs* on the Group
page (using the ``gs.group.home.interfaces.IGroupHomepageInfo``
manager).  Because the position of the About tab is so valuable
multiple products may want to show there. To allow this the About
viewlet contains a viewlet manager,
``gs.group.about.interfaces.IGroupAboutInfo``, which other products
(notably ``gs.group.encouragement``) can supply viewlets for.

The "normal" text of the About page is a viewlet that uses the
``IGroupAboutInfo`` manager. It gets its content from the
``aboutText`` property of the group.


The Change Page
===============

The *Change the About Tab* page is a simple form that changes the
``aboutText`` property of the group. This module provides the *Change*
page itself — and the link from the *Properties* list in the *Admin*
tab on the *Group* page to the *Change* page.
