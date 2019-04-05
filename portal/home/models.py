from django.db import models

from wagtail.core.models import Page

from portal.settings import GA_TAG


class HomePage(Page):

    def get_context(self, request):
        context = super().get_context(request)
        context.update({
            'GA_TAG': GA_TAG,
        })
        return context
