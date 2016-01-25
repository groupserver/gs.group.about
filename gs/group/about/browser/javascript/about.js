'use strict';
// Group page About-box JavaScript
//
// Copyright © 2013, 2014 OnlineGroups.net and Contributors.
// All Rights Reserved.
//
// This software is subject to the provisions of the Zope Public License,
// Version 2.1 (ZPL). http://groupserver.org/downloads/license/
//
// THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
// WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
// FITNESS FOR A PARTICULAR PURPOSE.
jQuery.noConflict();

function gs_group_about_init() {
    GSMoreWidget('#gs-group-about-tab-intro');
}

jQuery(window).load(function() {
    gsJsLoader.with_module('/++resource++gs-content-js-more-min-20160125.js',
                           gs_group_about_init);
});
