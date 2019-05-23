# from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError

from wagtail.core.models import Site

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('new_domain', type=str)

    def handle(self, *args, **options):
        new_domain = options['new_domain']
        self.stdout.write(self.style.SUCCESS(new_domain))
        s = Site.objects.all()[0]
        s.hostname = new_domain
        s.save()
