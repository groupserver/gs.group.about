jQuery.noConflict();

var setup_about = function () {
    GSMoreWidget('#gs-group-about-tab-intro');
}

jQuery(window).load(function () {
    gsJsLoader.with('/++resource++gs-content-js-more-20130110.js',
                    setup_about);
});
