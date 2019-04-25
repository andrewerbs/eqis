from django.utils.translation import gettext as _

from wagtail.core.blocks import (
    BlockQuoteBlock, CharBlock, RichTextBlock, StructBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class QuoteWithAttributionBlock(StructBlock):
    _quote_help_text = _("The quote's body text.")
    _attribution_help_text = _('Whom or what the text quotes.')

    quote = BlockQuoteBlock(
        label=_('Quote Text'),
        help_text=_quote_help_text,
    )
    attribution = CharBlock(
        label=_('Attribution'),
        required=False,
        max_length=255,
        help_text=_attribution_help_text,
    )

    class Meta:
        template = 'home/quote_with_attribution.html'


class PostcardBlock(StructBlock):
    _title_help_text = _("The description's title.")
    _image_help_text = _('An image that the description will accompany.')
    _description_help_text = _('Text that describes or accompanies the image.')

    _rich_text_features = ['bold', 'italic', 'link']

    title = CharBlock(
        label=_('Title'),
        max_length=255,
        required=False,
        help_text=_title_help_text,
    )
    image = ImageChooserBlock(
        label=_('Image'),
        help_text=_image_help_text,
    )
    description = RichTextBlock(
        label=_('Description'),
        features=_rich_text_features,
        help_text=_description_help_text,
    )

    class Meta:
        template = 'home/postcard_block.html'
