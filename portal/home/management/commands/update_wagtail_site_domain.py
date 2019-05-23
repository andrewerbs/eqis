# from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError

from wagtail.core.models import Site


class Command(BaseCommand):
    help = 'Updates the Wagtail site with a user-provided domain.'

    def add_arguments(self, parser):
        parser.add_argument('new_domain', type=str)

    def handle(self, *args, **options):
        new_domain = options['new_domain']
        s = Site.objects.all()[0]
        s.hostname = new_domain
        s.save()
        self.stdout.write(
            f'Site is now at the domain, {self.style.SUCCESS(new_domain)}.'
        )
