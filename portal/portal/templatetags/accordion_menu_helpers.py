from django import template


register = template.Library()


class AccordionMenuEntry:
    def __init__(self, a_wagtail_page, current_page):
        self._page_title = str(a_wagtail_page.homepage.translated_title) or ""
        self._page_url = a_wagtail_page.url if a_wagtail_page is not None else ""
        self._children = []
        self._is_active = False
        self._depth_first_copy(a_wagtail_page, current_page)

    @property
    def title(self):
        return self._page_title

    @property
    def url(self):
        return self._page_url

    @property
    def children(self):
        return self._children

    @property
    def active(self):
        return self._is_active

    def number_of_children(self):
        return len(self.children)

    def add_child(self, child):
        self._children.append(child)

    def __repr__(self):
        return f"<{self.title} is_active={self.active}>"

    def _depth_first_copy(self, a_wagtail_page, current_page):
        if a_wagtail_page is None:
            return

        if a_wagtail_page.url == current_page.url:
            self._is_active = True

        if a_wagtail_page.numchild > 0:
            for child in a_wagtail_page.get_children().live().in_menu():
                accordion_child = AccordionMenuEntry(child, current_page)
                self._is_active = self.active or accordion_child.active
                self.add_child(accordion_child)


@register.simple_tag(takes_context=True)
def get_accordion_menu(context, current_page):
    wagtail_site_root = context['request'].site.root_page
    accordion_menu = AccordionMenuEntry(wagtail_site_root, current_page)
    return {
        'current_page': current_page,
        'tree': accordion_menu,
    }
