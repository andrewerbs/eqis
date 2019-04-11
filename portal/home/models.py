from django.db import models
from django.utils import translation

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from portal.settings import GA_TAG


class TranslatedField:
    def __init__(self, en_field, my_field):
        self.en_field = en_field
        self.my_field = my_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'my':
            return getattr(instance, self.my_field)
        else:
            return getattr(instance, self.en_field)


class HomePage(Page):
    title_my = models.CharField(max_length=255, blank=True)

    description_en = RichTextField(blank=True)
    description_my = RichTextField(blank=True)

    translated_title = TranslatedField(
        'title',
        'title_my',
    )

    description = TranslatedField(
        'description_en',
        'description_my',
    )

    content_panels = Page.content_panels + [
        FieldPanel('title_my'),
        FieldPanel('description_en'),
        FieldPanel('description_my'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context.update({
            'GA_TAG': GA_TAG,
        })
        return context
