from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse
from django.utils.html import format_html

from wagtail.core import hooks
from wagtail.admin.menu import MenuItem


@hooks.register('register_admin_menu_item')
def register_link_to_superset_menu_item():
    return MenuItem(
        'My-EQIP Superset',
        'https://superset-myeqip.catalpa.build',
        classnames='icon icon-redirect',
        order=10000
    )
