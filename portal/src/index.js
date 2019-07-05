import './styles/main.scss';

const SEARCH_BAR_CSS_CLASS = 'search-bar';
const BACKGROUND_CSS_CLASS = 'background';
const TOP_PAGES_CSS_CLASS = 'top-pages';
const SIDEBAR_CSS_CLASS = 'sidebar';
const WIDGETS_CSS_CLASS = 'widgets';

export function toggle_sidebar() {
    if (is_visible(SIDEBAR_CSS_CLASS)) {
        hide(TOP_PAGES_CSS_CLASS);
        hide(BACKGROUND_CSS_CLASS);
        hide(SIDEBAR_CSS_CLASS);
        hide(WIDGETS_CSS_CLASS);
    } else {
        show(TOP_PAGES_CSS_CLASS);
        hide(SEARCH_BAR_CSS_CLASS);
        show(BACKGROUND_CSS_CLASS);
        show(SIDEBAR_CSS_CLASS);
        show(WIDGETS_CSS_CLASS);
    }
}

export function toggle_search_bar() {
    if (is_visible(SEARCH_BAR_CSS_CLASS)) {
        hide(SEARCH_BAR_CSS_CLASS);
        hide(BACKGROUND_CSS_CLASS);
    } else {
        show(SEARCH_BAR_CSS_CLASS);
        hide(TOP_PAGES_CSS_CLASS);
        show(BACKGROUND_CSS_CLASS);
        hide(SIDEBAR_CSS_CLASS);
        hide(WIDGETS_CSS_CLASS);
        focus(SEARCH_BAR_CSS_CLASS);
    }
}

function is_visible(element) {
    return window.getComputedStyle(document.getElementsByClassName(element).item(0)).display !== 'none';
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

function focus(element) {
    document.getElementsByClassName(element).item(0).getElementsByTagName('input').item(0).focus();
}
