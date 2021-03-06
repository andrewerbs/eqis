# models.py helper classes that contain all user-facing model strings.

from django.utils.translation import gettext as _


# Model Field Verbose Names
class _ModelVerboseNames:
    title = _("Title")
    description = _("Description")
    hero_image = _("Hero Image")
    body = _('Body')


# Model Field `help_text`s
class _ModelHelpTexts:
    title = _('''
    This title displays in browser tab headings, CardLinks, and searches.
    ''')
    description = _('''
    A short description of the web page. CardLinks display the description.
    ''')
    hero_image = _('''
        When CardLinks link to this web page, they show this image.
    ''')
    body = _('''
    The web page's contents. Pages define content as "blocks". Content blocks
    are: Titles; RichTexts; Postcards; CardLinks; or Quotes.
    ''')


# Streamfield blocks' names.
class _BlockNames:
    cardlink = _('CardLinks')
    postcard = _('Postcard')
    quote = _('Quote')
    rich_text = _('RichText')
    title = _('PageTitle')
    section_title = _('SectionTitle')
    line = _('Line')
    chart = _('Chart')


# Streamfield blocks' `help_text`s.
class _StreamfieldHelpTexts:
    title_block = _('''
    A title that displays full-width. The WebPage's body should start with
    a page title block. The title shows on a green background, or on a provided
    background image. The "Small Title" shows above the "Big Title".
    ''')
    section_title_block = _('''
    A section title that can be used anywhere in the page. The title has a
    green border line below.
    ''')
    rich_text = _('''
    Text that allows rich-formatted content: headers; bold and italic text;
    numbered and bulleted lists; hyperlinks; images; linked documents; and
    embedded web content.
    ''')
    postcard = _('''
    A card, resembling a postcard, that shows an image, a title, and a short
    text. The image covers half the card; the title and text cover the other
    half.
    ''')
    quote = _('''
    A quotation displayed in full width. The quotation shows its attribution
    below.
    ''')
    cardlink = _('''
    A richly styled link to an internal webpage. The link displays as a card
    that shows the linked-to website's hero image, title, and description.
    Many CardLinks can display in a responsive grid.
    ''')
    line_block = _('''
    A full-width line that separates blocks of content and shows as a green
    line on the web page.
    ''')
    chart_block = _('''
    A Superset chart from MyEQIP's superset instance. The drop-down menu
    lists available charts. The selected chart displays in the web page.
    ''')


# Content Panels
_english_panel = _('''
Content - English
''')
_myanmar_panel = _('''
Content - Myanmar
''')
_promote_panel = _('''
Promote
''')
_settings_panel = _('''
Settings
''')
