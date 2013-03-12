==================
``gs.group.about``
==================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The About box for a GroupServer Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-03-12
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

The *About* tab on the *Group* page provides some general information about
the group. This product supplies two things: a `viewlet`_ for the Group
page, and the `change Page`_ that allows the contents of the viewlet to be
altered.

Viewlet
=======

The *About Viewlet* is displayed in the main part the Group page [#group]_.
Because the position of the About tab is so valuable multiple products may
want to show there. To allow this the About viewlet contains a viewlet
manager, ``gs.group.about.interfaces.IGroupAboutInfo``, which other
products can supply viewlets for.

The "normal" text of the About page is a viewlet that uses the
``IGroupAboutInfo`` manager. It gets its content from the ``aboutText``
property of the group. A more button [#more]_ is used to stop the content
of the About Viewlet overwhelming the page.

Another viewlet is used to link to `Change Page`_ if the viewer is a group
administrator.

Change Page
===========

The *Change About* page is a simple form that changes the ``aboutText``
property of the group. This module provides the *Change* page itself — and
the link from the *Properties* list in the *Admin* tab on the *Group* page
to the *Change* page. Most group-property pages can only be changed by the
site administrator, but an exception is made for the *About*, which can be
changed by the group administrator.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.about
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

..  [#group] See ``gs.group.home``.
..  [#more] See ``gs.content.js.more``.
