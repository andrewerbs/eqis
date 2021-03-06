# Generated by Django 2.1.8 on 2019-05-13 01:23

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial_database_rc003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('cardlink', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(can_choose_root=False, help_text="\n    The CardLink will link to this page. The card displays the page's hero\n    image and description.\n    ", label='Choose a page', page_type=['home.WebPage']))], help_text="\n    A richly styled link to an internal webpage. The link displays as a card that\n    shows the linked-to website's hero image, title, and description. Many\n    CardLinks can display in a responsive grid.\n    ", label='CardLinks'), template='home/list_block_card_link.html')), ('postcard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='The Postcard\'s title sits above the "description".', label='Title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The description accompanies this image.', label='Image')), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Text that accompanies the image.', label='Description'))], help_text='\n    A card, resembling a postcard, that shows an image, a title, and a short\n    text. The image covers half the card; the title and text cover the other\n    half.\n    ', label='Postcard')), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.BlockQuoteBlock(help_text="The quote's body text.", label='Quote Text')), ('attribution', wagtail.core.blocks.CharBlock(help_text='Whom or what the text quotes.', label='Attribution', max_length=255, required=False))], help_text='\n    A quotation displayed in full width. The quotation shows its attribution\n    below.\n    ', label='Quote')), ('rich_text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'], help_text='\n    Text that allows rich-formatted content: headers; bold and italic text;\n    numbered and bulleted lists; hyperlinks; images; linked documents; and\n    embedded web content.\n    ', label='RichText')), ('title', wagtail.core.blocks.StructBlock([('big_title', wagtail.core.blocks.CharBlock(help_text='\n    This shows below the Small Title. It has bigger text.\n    ', label='The Big Title', max_length=255)), ('small_title', wagtail.core.blocks.CharBlock(help_text="\n    'This shows above the Big Title. It has smaller text.\n    ", label='The Small Title', max_length=255))], help_text='\n    A title that displays full-width. The WebPage\'s body should start with this\n    title. The "Small Title" shows above the "Big Title".\n    ', label='Title'))], blank=True, help_text='\n    The web page\'s contents. Pages define content as "blocks". Content blocks\n    are: Titles; RichTexts; Postcards; CardLinks; or Quotes.\n    ', verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='body_my',
            field=wagtail.core.fields.StreamField([('cardlink', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock(can_choose_root=False, help_text="\n    The CardLink will link to this page. The card displays the page's hero\n    image and description.\n    ", label='Choose a page', page_type=['home.WebPage']))], help_text="\n    A richly styled link to an internal webpage. The link displays as a card that\n    shows the linked-to website's hero image, title, and description. Many\n    CardLinks can display in a responsive grid.\n    ", label='CardLinks'), template='home/list_block_card_link.html')), ('postcard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='The Postcard\'s title sits above the "description".', label='Title', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The description accompanies this image.', label='Image')), ('description', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Text that accompanies the image.', label='Description'))], help_text='\n    A card, resembling a postcard, that shows an image, a title, and a short\n    text. The image covers half the card; the title and text cover the other\n    half.\n    ', label='Postcard')), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.BlockQuoteBlock(help_text="The quote's body text.", label='Quote Text')), ('attribution', wagtail.core.blocks.CharBlock(help_text='Whom or what the text quotes.', label='Attribution', max_length=255, required=False))], help_text='\n    A quotation displayed in full width. The quotation shows its attribution\n    below.\n    ', label='Quote')), ('rich_text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'], help_text='\n    Text that allows rich-formatted content: headers; bold and italic text;\n    numbered and bulleted lists; hyperlinks; images; linked documents; and\n    embedded web content.\n    ', label='RichText')), ('title', wagtail.core.blocks.StructBlock([('big_title', wagtail.core.blocks.CharBlock(help_text='\n    This shows below the Small Title. It has bigger text.\n    ', label='The Big Title', max_length=255)), ('small_title', wagtail.core.blocks.CharBlock(help_text="\n    'This shows above the Big Title. It has smaller text.\n    ", label='The Small Title', max_length=255))], help_text='\n    A title that displays full-width. The WebPage\'s body should start with this\n    title. The "Small Title" shows above the "Big Title".\n    ', label='Title'))], blank=True, help_text='\n    The web page\'s contents. Pages define content as "blocks". Content blocks\n    are: Titles; RichTexts; Postcards; CardLinks; or Quotes.\n    ', verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='description_en',
            field=models.TextField(blank=True, help_text='\n    A short description of the web page. CardLinks display the description.\n    ', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='description_my',
            field=models.TextField(blank=True, help_text='\n    A short description of the web page. CardLinks display the description.\n    ', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='\n        When CardLinks link to this web page, they show this image.\n    ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Hero Image'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='title_my',
            field=models.CharField(blank=True, help_text='\n    This title displays in browser tab headings, CardLinks, and searches.\n    ', max_length=255, verbose_name='Title'),
        ),
    ]
