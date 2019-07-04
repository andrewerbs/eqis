from django.db import models
from django.utils.translation import get_language

from wagtail.admin.edit_handlers import (
    FieldPanel, ObjectList, StreamFieldPanel, TabbedInterface
)
from wagtail.core.blocks import ListBlock, RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from .blocks import (
    CardLinkBlock, ChartBlock, LineBlock, PostcardBlock,
    QuoteWithAttributionBlock, TitleBlock, SectionTitleBlock
)
from .models_ui_text import (
    _english_panel, _myanmar_panel, _promote_panel, _settings_panel,
    _BlockNames, _ModelHelpTexts, _StreamfieldHelpTexts, _ModelVerboseNames
)


class TranslatedField:
    def __init__(self, en_field, my_field):
        self.en_field = en_field
        self.my_field = my_field

    def _get_translated_field_or_fallback(self, local_language, fallback):
        return local_language if len(local_language) > 0 else fallback

    def __get__(self, instance, owner):
        in_myanmar = getattr(instance, self.my_field)
        in_english = getattr(instance, self.en_field)

        if get_language() == 'my':
            return self._get_translated_field_or_fallback(
                local_language=in_myanmar,
                fallback=in_english
            )
        else:
            return self._get_translated_field_or_fallback(
                local_language=in_english,
                fallback=in_myanmar
            )


class WebPage(Page):

    # Values that help Streamfield Blocks.
    _rich_text_features = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold',
                           'italic', 'ol', 'ul', 'link',
                           'document-link', 'image', 'embed']
    _block_list = [
        (
            'CardLinks',
            ListBlock(
                CardLinkBlock(
                    label=_BlockNames.cardlink,
                    help_text=_StreamfieldHelpTexts.cardlink,
                ),
                template='home/list_block_card_link.html',
            ),
        ),
        (
            'Postcard',
            PostcardBlock(
                label=_BlockNames.postcard,
                help_text=_StreamfieldHelpTexts.postcard,
            ),
        ),
        (
            'Quote',
            QuoteWithAttributionBlock(
                label=_BlockNames.quote,
                help_text=_StreamfieldHelpTexts.quote,
            ),
        ),
        (
            'RichText',
            RichTextBlock(
                features=_rich_text_features,
                label=_BlockNames.rich_text,
                help_text=_StreamfieldHelpTexts.rich_text,
            ),
        ),
        (
            'Title',
            TitleBlock(
                label=_BlockNames.title,
                help_text=_StreamfieldHelpTexts.title_block,
            ),
        ),
        (
            'SectionTitle',
            SectionTitleBlock(
                label=_BlockNames.section_title,
                help_text=_StreamfieldHelpTexts.section_title_block,
            ),
        ),
        (
            'Line',
            LineBlock(
                label=_BlockNames.line,
                help_text=_StreamfieldHelpTexts.line_block,
            ),
        ),
        (
            'Chart',
            ChartBlock(
                label=_BlockNames.chart,
                help_text=_StreamfieldHelpTexts.chart_block,
            ),
        ),
    ]

    # Model Fields
    title_my = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_ModelVerboseNames.title,
        help_text=_ModelHelpTexts.title,
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_ModelVerboseNames.hero_image,
        help_text=_ModelHelpTexts.hero_image,
    )
    description_en = models.TextField(
        blank=True,
        verbose_name=_ModelVerboseNames.description,
        help_text=_ModelHelpTexts.description,
    )
    description_my = models.TextField(
        blank=True,
        verbose_name=_ModelVerboseNames.description,
        help_text=_ModelHelpTexts.description,
    )

    body_en = StreamField(
        _block_list,
        blank=True,
        help_text=_ModelHelpTexts.body,
        verbose_name=_ModelVerboseNames.body,
    )
    body_my = StreamField(
        _block_list,
        blank=True,
        help_text=_ModelHelpTexts.body,
        verbose_name=_ModelVerboseNames.body,
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
        ObjectList(en_content_panels, heading=_english_panel),
        ObjectList(my_content_panels, heading=_myanmar_panel),
        ObjectList(promote_panels, heading=_promote_panel),
        ObjectList(
            Page.settings_panels,
            heading=_settings_panel,
            classname="settings"
        ),
    ])
