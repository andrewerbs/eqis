from django.utils.html import mark_safe
from django.utils.translation import gettext as _

from wagtail.core.blocks import (
    BlockQuoteBlock, CharBlock, PageChooserBlock, RichTextBlock, StaticBlock,
    StructBlock
)
from wagtail.images.blocks import ImageChooserBlock

from .blocks_ui_text import (
    _PostcardStrings, _TitleStrings, _CardLinkStrings, _QuoteStrings
)


class QuoteWithAttributionBlock(StructBlock):

    quote = BlockQuoteBlock(
        label=_QuoteStrings.quote_label,
        help_text=_QuoteStrings.quote_help_text,
    )
    attribution = CharBlock(
        label=_QuoteStrings.attribution_label,
        required=False,
        max_length=255,
        help_text=_QuoteStrings.attribution_help_text,
    )

    class Meta:
        template = 'home/quote_with_attribution.html'


class PostcardBlock(StructBlock):

    _rich_text_features = ['bold', 'italic', 'link']

    title = CharBlock(
        label=_PostcardStrings.title_label,
        max_length=255,
        required=False,
        help_text=_PostcardStrings.title_help_text,
    )
    image = ImageChooserBlock(
        label=_PostcardStrings.image_label,
        help_text=_PostcardStrings.image_help_text,
    )
    description = RichTextBlock(
        label=_PostcardStrings.description_label,
        features=_rich_text_features,
        help_text=_PostcardStrings.description_help_text,
    )

    class Meta:
        template = 'home/postcard_block.html'


class TitleBlock(StructBlock):
    big_title = CharBlock(
        label=_TitleStrings.big_title_label,
        help_text=_TitleStrings.big_title_help_text,
        max_length=255,
    )
    small_title = CharBlock(
        label=_TitleStrings.small_title_label,
        help_text=_TitleStrings.small_title_help_text,
        max_length=255,
    )

    class Meta:
        template = 'home/title_block.html'


class CardLinkBlock(StructBlock):
    page = PageChooserBlock(
        label=_CardLinkStrings.page_chooser_label,
        help_text=_CardLinkStrings.page_chooser_help_text,
        can_choose_root=False,
        target_model="home.WebPage",
    )

    class Meta:
        template = 'home/card_link_block.html'


class LineBlock(StaticBlock):
    class Meta:
        template = 'home/line_block.html'
