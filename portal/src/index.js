import './styles/main.scss';

const MOBILE_HEADER_CSS_CLASS = 'mobile-header';
const SEARCH_BAR_CSS_CLASS = 'search-bar';
const BACKGROUND_CSS_CLASS = 'background';
const TOP_PAGES_CSS_CLASS = 'top-pages';
const SIDEBAR_CSS_CLASS = 'sidebar';

export function toggle_sidebar() {
    if (is_visible(SIDEBAR_CSS_CLASS)) {
        hide(MOBILE_HEADER_CSS_CLASS, TOP_PAGES_CSS_CLASS);
        hide(BACKGROUND_CSS_CLASS);
        hide(SIDEBAR_CSS_CLASS);
    } else {
        show(MOBILE_HEADER_CSS_CLASS, TOP_PAGES_CSS_CLASS, SEARCH_BAR_CSS_CLASS);
        show(BACKGROUND_CSS_CLASS);
        show(SIDEBAR_CSS_CLASS);
    }
}

export function toggle_search_bar() {
    if (is_visible(SEARCH_BAR_CSS_CLASS)) {
        hide(MOBILE_HEADER_CSS_CLASS, SEARCH_BAR_CSS_CLASS);
        hide(BACKGROUND_CSS_CLASS);
    } else {
        show(MOBILE_HEADER_CSS_CLASS, SEARCH_BAR_CSS_CLASS, TOP_PAGES_CSS_CLASS);
        show(BACKGROUND_CSS_CLASS);
        hide(SIDEBAR_CSS_CLASS);
    }
}

function is_visible(element_css_class) {
    return window.getComputedStyle(document.getElementsByClassName(element_css_class).item(0)).display !== "none";
}

function show(element_css_class, to_show, to_hide) {
    if (element_css_class === MOBILE_HEADER_CSS_CLASS) {
        document.getElementsByClassName(to_hide).item(0).classList.remove('d-flex');
        document.getElementsByClassName(to_show).item(0).classList.add('d-flex');
    }

    document.getElementsByClassName(element_css_class).item(0).classList.remove('d-none');
}

function hide(element_css_class, to_hide) {
    if (element_css_class === MOBILE_HEADER_CSS_CLASS) document.getElementsByClassName(to_hide).item(0).classList.remove('d-flex');

    document.getElementsByClassName(element_css_class).item(0).classList.add('d-none');
}
