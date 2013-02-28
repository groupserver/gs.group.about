jQuery.noConflict();

function gs_group_about_change_init() {
    //jQuery('#form\\.actions\\.change').addClass('btn').button();
    
}

jQuery(window).load(function () {
    var modules = ['/++resource++wymeditor-20090831/jquery.wymeditor.js',
                   '/++resource++gswym.js'];
    gsJsLoader.with_module(modules, gs_group_about_change_init);
});