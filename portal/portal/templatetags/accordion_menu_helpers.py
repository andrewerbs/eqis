from django import template
from django.utils.safestring import mark_safe

from wagtail.core.models import Page


register = template.Library()


class AccordionMenuEntry:
    def __init__(self, a_wagtail_page=None):
        self._page_title = str(a_wagtail_page) or ""
        self._page_url = a_wagtail_page.url or ""
        self._active_page = False
        self._children = []
        self._depth_first_copy(a_wagtail_page)

    @property
    def title(self):
        return self._page_title

    @property
    def url(self):
        return self._page_url

    @property
    def children(self):
        return self._children

    def number_of_children(self):
        return len(self.children)

    def add_child(self, child):
        self._children.append(child)

    def __str__(self):
        return self._page_title

    def _depth_first_copy(self, a_wagtail_page):
        if a_wagtail_page is None:
            return
        if a_wagtail_page.numchild > 0:
            for child in a_wagtail_page.get_children().live():
                self.add_child(AccordionMenuEntry(child))


@register.filter
def is_page_active(accordion_entry, wagtail_page):
    return accordion_entry.title == str(wagtail_page)


@register.inclusion_tag('home/accordion_menu.html')
def create_accordion_menu_from_site_map(current_page):
    all_live_pages = Page.objects.live()
    # Accordion Menu starts at Home Page.
    accordion_menu = AccordionMenuEntry(all_live_pages[1])

    return {
        'current_page': current_page,
        'pages': accordion_menu,
    }
