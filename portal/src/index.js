import './styles/main.scss';

const SEARCH_BAR_CSS_CLASS = 'search-bar';
const BACKGROUND_CSS_CLASS = 'background';
const TOP_PAGES_CSS_CLASS = 'top-pages';
const SIDEBAR_CSS_CLASS = 'sidebar';
const WIDGETS_CSS_CLASS = 'widgets';
const CONTENT_CSS_CLASS = 'content';
const ESCAPE_KEY = 'Escape';

export function toggle_sidebar() {
    if (is_visible(SIDEBAR_CSS_CLASS)) hide_sidebar();
    else show_sidebar();
}

export function toggle_search_bar() {
    if (is_visible(SEARCH_BAR_CSS_CLASS)) hide_search_bar();
    else show_search_bar();
}

function is_visible(element_css_class) {
    return window.getComputedStyle(document.getElementsByClassName(element_css_class).item(0)).display !== 'none';
}

function show_sidebar() {
    show(TOP_PAGES_CSS_CLASS);
    hide(SEARCH_BAR_CSS_CLASS);
    show(BACKGROUND_CSS_CLASS);
    show(SIDEBAR_CSS_CLASS);
    show(WIDGETS_CSS_CLASS);
    attachClickEvent(BACKGROUND_CSS_CLASS, hide_sidebar);
}

function hide_sidebar() {
    hide(TOP_PAGES_CSS_CLASS);
    hide(BACKGROUND_CSS_CLASS);
    hide(SIDEBAR_CSS_CLASS);
    hide(WIDGETS_CSS_CLASS);
}

function show_search_bar() {
    show(SEARCH_BAR_CSS_CLASS);
    hide(TOP_PAGES_CSS_CLASS);
    show(BACKGROUND_CSS_CLASS);
    hide(SIDEBAR_CSS_CLASS);
    hide(WIDGETS_CSS_CLASS);
    focus(SEARCH_BAR_CSS_CLASS);
    attachClickEvent(BACKGROUND_CSS_CLASS, hide_search_bar);
    attachClickEvent(CONTENT_CSS_CLASS, hide_search_bar);
    attachEscapeKeyEvent(hide_search_bar);
}

function hide_search_bar() {
    hide(SEARCH_BAR_CSS_CLASS);
    hide(BACKGROUND_CSS_CLASS);
}

function show(to_show) {
    if (to_show === WIDGETS_CSS_CLASS) document.getElementsByClassName(to_show).item(0).classList.add('d-flex');
    else if (to_show === SIDEBAR_CSS_CLASS || to_show === BACKGROUND_CSS_CLASS) document.getElementsByClassName(to_show).item(0).classList.remove('d-none');
    else document.getElementsByClassName(to_show).item(0).classList.add('d-block');
}

function hide(to_hide) {
    if (to_hide === TOP_PAGES_CSS_CLASS || to_hide === SEARCH_BAR_CSS_CLASS) document.getElementsByClassName(to_hide).item(0).classList.remove('d-block');
    else if (to_hide === WIDGETS_CSS_CLASS) document.getElementsByClassName(to_hide).item(0).classList.remove('d-flex');
    else document.getElementsByClassName(to_hide).item(0).classList.add('d-none');
}

function focus(element_css_class) {
    document.getElementsByClassName(element_css_class).item(0).getElementsByTagName('input').item(0).focus();
}

function attachClickEvent(element_css_class, hide) {
    var element = document.getElementsByClassName(element_css_class).item(0);

    element.addEventListener('click', function contentClickEvent() {
        hide();
        element.removeEventListener('click', contentClickEvent);
    });
}

function attachEscapeKeyEvent(hide) {
    document.addEventListener('keyup', function escapeKeyEvent(event) {
        if (event.key === ESCAPE_KEY) {
            hide();
            document.removeEventListener('keyup', escapeKeyEvent);
        }
    });
}
