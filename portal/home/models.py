from django.db import models
from django.utils.translation import get_language, gettext as _

from portal.settings import GA_TAG
from wagtail.admin.edit_handlers import (
    FieldPanel, StreamFieldPanel, TabbedInterface, ObjectList
)
from wagtail.core.blocks import BlockQuoteBlock, RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index

from .blocks import QuoteWithAttributionBlock


class TranslatedField:
    def __init__(self, en_field, my_field):
        self.en_field = en_field
        self.my_field = my_field

    def __get__(self, instance, owner):
        if get_language() == 'my':
            return getattr(instance, self.my_field)
        else:
            return getattr(instance, self.en_field)


class HomePage(Page):
    title_my = models.CharField(
        max_length=255, blank=True, verbose_name=_("title"))
    translated_title = TranslatedField(
        'title',
        'title_my',
    )

    _rich_text_features = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic',
                           'ol', 'ul', 'link', 'document-link', 'image', 'embed']
    _body_verbose_name = _('body')
    _body_help_text = _('''
    You can create page content with "blocks". With the "RichText" block, you
    can write with headers, bold and italic text, lists, images, anchors,
    document links, and embed links.
    ''')
    _rich_text_block_name = _('RichText')
    _quote_block_name = _('Quote')

    body_en = StreamField(
        [
            (_rich_text_block_name, RichTextBlock(features=_rich_text_features)),
            (_quote_block_name, QuoteWithAttributionBlock()),
        ],
        blank=True,
        help_text=_body_help_text,
        verbose_name=_body_verbose_name,
    )
    body_my = StreamField(
        [
            (_rich_text_block_name, RichTextBlock(features=_rich_text_features)),
            (_quote_block_name, QuoteWithAttributionBlock()),
        ],
        blank=True,
        help_text=_body_help_text,
        verbose_name=_body_verbose_name,
    )
    body = TranslatedField(
        'body_en',
        'body_my',
    )

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('title_my'),
        index.SearchField('body_en'),
        index.SearchField('body_my'),
    ]

    en_content_panels = Page.content_panels + [
        StreamFieldPanel('body_en'),
    ]
    my_content_panels = [
        FieldPanel('title_my'),
        StreamFieldPanel('body_my'),
    ]
    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading=_('Content - English')),
        ObjectList(my_content_panels, heading=_('Content - Myanmar')),
        ObjectList(Page.promote_panels, heading=_('Promote')),
        ObjectList(
            Page.settings_panels,
            heading=_('Settings'),
            classname="settings"
        ),
    ])

    def get_context(self, request):
        context = super().get_context(request)
        context.update({
            'GA_TAG': GA_TAG,
        })
        return context
