from django.db import models
from django.utils.translation import get_language, gettext as _

from portal.settings import GA_TAG
from wagtail.admin.edit_handlers import (
    FieldPanel, ObjectList, StreamFieldPanel, TabbedInterface
)
from wagtail.core.blocks import BlockQuoteBlock, ListBlock, RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from .blocks import (
    CardLinkBlock, PostcardBlock, QuoteWithAttributionBlock, TitleBlock
)


class TranslatedField:
    def __init__(self, en_field, my_field):
        self.en_field = en_field
        self.my_field = my_field

    def __get__(self, instance, owner):
        if get_language() == 'my':
            return getattr(instance, self.my_field)
        else:
            return getattr(instance, self.en_field)


class WebPage(Page):
    # Model Field Verbose Names
    _hero_image_verbose_name = _("Hero Image")
    _description_verbose_name = _("Description")
    _body_verbose_name = _('body')

    # Model Field Help Text.
    _hero_image_help_text = _("This image displays at the top of the page.")
    _body_help_text = _('''
    You can create page content with "blocks". With the "RichText" block, you
    can write with headers, bold and italic text, lists, images, anchors,
    document links, and embed links.
    ''')

    # Values that help Streamfield Blocks.
    _rich_text_features = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic',
                           'ol', 'ul', 'link', 'document-link', 'image', 'embed']
    _card_link_blocks_name = _('CardLinks')
    _postcard_block_name = _('Postcard')
    _quote_block_name = _('Quote')
    _rich_text_block_name = _('RichText')
    _title_block_name = _('Title')
    _block_list = [
        (_card_link_blocks_name, ListBlock(
            CardLinkBlock(),
            template='home/list_block_card_link.html'
        )),
        (_postcard_block_name, PostcardBlock()),
        (_quote_block_name, QuoteWithAttributionBlock()),
        (_rich_text_block_name, RichTextBlock(features=_rich_text_features)),
        (_title_block_name, TitleBlock()),
    ]

    # Model Fields
    title_my = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("title")
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description_en = models.TextField(
        blank=True,
        verbose_name=_description_verbose_name
    )
    description_my = models.TextField(
        blank=True,
        verbose_name=_description_verbose_name
    )

    body_en = StreamField(
        _block_list,
        blank=True,
        help_text=_body_help_text,
        verbose_name=_body_verbose_name,
    )
    body_my = StreamField(
        _block_list,
        blank=True,
        help_text=_body_help_text,
        verbose_name=_body_verbose_name,
    )

    # Translatable fields.
    translated_title = TranslatedField(
        'title',
        'title_my',
    )
    description = TranslatedField(
        'description_en',
        'description_my',
    )
    body = TranslatedField(
        'body_en',
        'body_my',
    )

    # Add fields to the search index.
    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('title_my'),
        index.SearchField('body_en'),
        index.SearchField('body_my'),
        index.SearchField('description_en'),
        index.SearchField('description_my')
    ]

    # Which fields the English and Myanmar admin tabs display.
    en_content_panels = Page.content_panels + [
        FieldPanel('description_en'),
        StreamFieldPanel('body_en'),
    ]
    my_content_panels = [
        FieldPanel('title_my'),
        FieldPanel('description_my'),
        StreamFieldPanel('body_my'),
    ]
    promote_panels = Page.promote_panels + [
        ImageChooserPanel('hero_image'),
    ]

    # Sets the Wagtail Admin Interface's tabs.
    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading=_('Content - English')),
        ObjectList(my_content_panels, heading=_('Content - Myanmar')),
        ObjectList(promote_panels, heading=_('Promote')),
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
