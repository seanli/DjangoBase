from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    args = '< any argument >'
    help = 'Test Command.'

    def handle(self, *args, **options):
        if len(args) == 0:
            raise CommandError('Please at least pass in one argument.')
        else:
            for arg in args:
                print arg
