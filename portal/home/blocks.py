from django.utils.translation import gettext as _

from wagtail.core.blocks import (
    BlockQuoteBlock, CharBlock, PageChooserBlock, RichTextBlock, StructBlock
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


class TitleBlock(StructBlock):
    _big_title_help_text = _('This title displays larger in the block.')
    _small_title_help_text = _('This title displays smaller in the block.')

    _big_title_label = _('The Big Title')
    _small_title_label = _('The Small Title')

    big_title = CharBlock(
        label=_big_title_label,
        help_text=_big_title_help_text,
        max_length=255,
    )
    small_title = CharBlock(
        label=_small_title_label,
        help_text=_small_title_help_text,
        max_length=255,
    )

    class Meta:
        template = 'home/title_block.html'


class CardLinkBlock(StructBlock):
    _page_help_text = _('''
    The CardLink will link to this page. The card displays the page's hero
    image and description.
    ''')

    page = PageChooserBlock(
        label=_('Choose a page'),
        help_text=_page_help_text,
        can_choose_root=False,
        target_model="home.HomePage",
    )

    class Meta:
        template = 'home/card_link_block.html'
