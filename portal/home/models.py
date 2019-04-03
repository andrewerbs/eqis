from django.db import models

from wagtail.core.models import Page

from portal.settings import GA_TAG


class HomePage(Page):

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context.update({
            'GA_TAG': GA_TAG,
        })
        return context
