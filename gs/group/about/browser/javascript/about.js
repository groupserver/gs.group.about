jQuery.noConflict();

function gs_group_about_init () {
    GSMoreWidget('#gs-group-about-tab-intro');
}

jQuery(window).load(function () {
    gsJsLoader.with_module('/++resource++gs-content-js-more-20130110.js',
                           gs_group_about_init)});