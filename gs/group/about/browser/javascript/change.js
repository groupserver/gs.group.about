"use strict";
// Change About JavaScript
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

function gs_group_about_change_init() {
    //jQuery('#form\\.actions\\.change').addClass('btn').button();
    
}

jQuery(window).load(function () {
    var modules = ['/++resource++wymeditor-20090831/jquery.wymeditor.js',
                   '/++resource++gswym.js'];
    gsJsLoader.with_module(modules, gs_group_about_change_init);
});