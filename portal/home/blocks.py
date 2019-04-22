from django.utils.translation import gettext as _

from wagtail.core.blocks import BlockQuoteBlock, CharBlock, StructBlock


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
