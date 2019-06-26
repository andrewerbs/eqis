# blocks.py helper classes that contain all user-facing block strings.

from django.utils.translation import gettext as _


# QuoteBlock
class _QuoteStrings:
    quote_label = _('Quote Text')
    quote_help_text = _("The quote's body text.")
    attribution_label = _('Attribution')
    attribution_help_text = _('Whom or what the text quotes.')


# PostcardBlock
class _PostcardStrings:
    title_label = _('Title')
    title_help_text = _("The Postcard's title sits above the \"description\".")
    image_label = _('Image')
    image_help_text = _('The description accompanies this image.')
    image_disposition_label = _('Image disposition')
    image_disposition_help_text = _('''
        Disposition of this image in relation with the text that accompanies.
    ''')
    image_disposition_right = _('On the right')
    image_disposition_left = _('On the left')
    description_label = _('Description')
    description_help_text = _('Text that accompanies the image.')


# TitleBlock
class _TitleStrings:
    big_title_help_text = _('''
    This shows below the Small Title. It has bigger text.
    ''')
    small_title_help_text = _('''
    This shows above the Big Title. It has smaller text.
    ''')
    big_title_label = _('The Big Title')
    small_title_label = _('The Small Title')
    image_label = _('Image')
    image_help_text = _('A screen-width image.')


# SectionTitleBlock
class _SectionTitleStrings:
    section_title_label = _('Title')
    section_title_help_text = _('The section title.')


# CardLinkBlock
class _CardLinkStrings:
    page_chooser_label = _('Choose a page')
    page_chooser_help_text = _('''
    The CardLink will link to this page. The card displays the page's hero
    image and description.
    ''')


#ChartBlock
class _ChartBlockStrings:
    title_label = _('Title')
    title_help_text = _("The chart's title.")
    description_label = _('Description')
    description_help_text = _("Describes the chart.")