# Generated by Django 2.1.8 on 2019-06-26 02:41

from django.db import migrations
import home.blocks
import home.superset_helpers
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_postcard_image_disposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('CardLinks', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(can_choose_root=False, help_text="\n    The CardLink will link to this page. The card displays the page's hero\n    image and description.\n    ", label='Choose a page', target_model=['home.WebPage']))], help_text="\n    A richly styled link to an internal webpage. The link displays as a card\n    that shows the linked-to website's hero image, title, and description.\n    Many CardLinks can display in a responsive grid.\n    ", label='CardLinks'), template='home/list_block_card_link.html')), ('Postcard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='The Postcard\'s title sits above the "description".', label='Title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The description accompanies this image.', label='Image')), ('image_disposition', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'On the left'), ('right', 'On the right')], help_text='\n        Disposition of this image in relation with the text that accompanies.\n    ', label='Image disposition')), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Text that accompanies the image.', label='Description'))], help_text='\n    A card, resembling a postcard, that shows an image, a title, and a short\n    text. The image covers half the card; the title and text cover the other\n    half.\n    ', label='Postcard')), ('Quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.BlockQuoteBlock(help_text="The quote's body text.", label='Quote Text')), ('attribution', wagtail.core.blocks.CharBlock(help_text='Whom or what the text quotes.', label='Attribution', max_length=255, required=False))], help_text='\n    A quotation displayed in full width. The quotation shows its attribution\n    below.\n    ', label='Quote')), ('RichText', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'], help_text='\n    Text that allows rich-formatted content: headers; bold and italic text;\n    numbered and bulleted lists; hyperlinks; images; linked documents; and\n    embedded web content.\n    ', label='RichText')), ('Title', wagtail.core.blocks.StructBlock([('small_title', wagtail.core.blocks.CharBlock(help_text='\n    This shows above the Big Title. It has smaller text.\n    ', label='The Small Title', max_length=255, required=False)), ('big_title', wagtail.core.blocks.CharBlock(help_text='\n    This shows below the Small Title. It has bigger text.\n    ', label='The Big Title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='A screen-width image.', label='Image', required=False))], help_text='\n    A title that displays full-width. The WebPage\'s body should start with\n    a page title block. The title shows on a green background, or on a provided\n    background image. The "Small Title" shows above the "Big Title".\n    ', label='PageTitle')), ('SectionTitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='The section title.', label='Title', max_length=255))], help_text='\n    A section title that can be used anywhere in the page. The title has a\n    green border line below.\n    ', label='SectionTitle')), ('Line', home.blocks.LineBlock(help_text='\n    A full-width line that separates blocks of content and shows as a green\n    line on the web page.\n    ', label='Line')), ('Chart', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text="The chart's title.", label='Title', max_length=255, required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Describes the chart.', label='Description', required=False)), ('choice_of_chart', wagtail.core.blocks.ChoiceBlock(choices=home.superset_helpers.get_superset_chart_choices))], help_text="\n    A Superset chart from MyEQIP's superset instance. The drop-down menu\n    lists available charts. The selected chart displays in the web page.\n    ", label='Chart'))], blank=True, help_text='\n    The web page\'s contents. Pages define content as "blocks". Content blocks\n    are: Titles; RichTexts; Postcards; CardLinks; or Quotes.\n    ', verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='body_my',
            field=wagtail.core.fields.StreamField([('CardLinks', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(can_choose_root=False, help_text="\n    The CardLink will link to this page. The card displays the page's hero\n    image and description.\n    ", label='Choose a page', target_model=['home.WebPage']))], help_text="\n    A richly styled link to an internal webpage. The link displays as a card\n    that shows the linked-to website's hero image, title, and description.\n    Many CardLinks can display in a responsive grid.\n    ", label='CardLinks'), template='home/list_block_card_link.html')), ('Postcard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='The Postcard\'s title sits above the "description".', label='Title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The description accompanies this image.', label='Image')), ('image_disposition', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'On the left'), ('right', 'On the right')], help_text='\n        Disposition of this image in relation with the text that accompanies.\n    ', label='Image disposition')), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Text that accompanies the image.', label='Description'))], help_text='\n    A card, resembling a postcard, that shows an image, a title, and a short\n    text. The image covers half the card; the title and text cover the other\n    half.\n    ', label='Postcard')), ('Quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.BlockQuoteBlock(help_text="The quote's body text.", label='Quote Text')), ('attribution', wagtail.core.blocks.CharBlock(help_text='Whom or what the text quotes.', label='Attribution', max_length=255, required=False))], help_text='\n    A quotation displayed in full width. The quotation shows its attribution\n    below.\n    ', label='Quote')), ('RichText', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'], help_text='\n    Text that allows rich-formatted content: headers; bold and italic text;\n    numbered and bulleted lists; hyperlinks; images; linked documents; and\n    embedded web content.\n    ', label='RichText')), ('Title', wagtail.core.blocks.StructBlock([('small_title', wagtail.core.blocks.CharBlock(help_text='\n    This shows above the Big Title. It has smaller text.\n    ', label='The Small Title', max_length=255, required=False)), ('big_title', wagtail.core.blocks.CharBlock(help_text='\n    This shows below the Small Title. It has bigger text.\n    ', label='The Big Title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='A screen-width image.', label='Image', required=False))], help_text='\n    A title that displays full-width. The WebPage\'s body should start with\n    a page title block. The title shows on a green background, or on a provided\n    background image. The "Small Title" shows above the "Big Title".\n    ', label='PageTitle')), ('SectionTitle', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='The section title.', label='Title', max_length=255))], help_text='\n    A section title that can be used anywhere in the page. The title has a\n    green border line below.\n    ', label='SectionTitle')), ('Line', home.blocks.LineBlock(help_text='\n    A full-width line that separates blocks of content and shows as a green\n    line on the web page.\n    ', label='Line')), ('Chart', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text="The chart's title.", label='Title', max_length=255, required=False)), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Describes the chart.', label='Description', required=False)), ('choice_of_chart', wagtail.core.blocks.ChoiceBlock(choices=home.superset_helpers.get_superset_chart_choices))], help_text="\n    A Superset chart from MyEQIP's superset instance. The drop-down menu\n    lists available charts. The selected chart displays in the web page.\n    ", label='Chart'))], blank=True, help_text='\n    The web page\'s contents. Pages define content as "blocks". Content blocks\n    are: Titles; RichTexts; Postcards; CardLinks; or Quotes.\n    ', verbose_name='Body'),
        ),
    ]