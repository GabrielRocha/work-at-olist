from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('channel', type=str, help="Channel name")
        parser.add_argument('categories_file', type=str, help="Categories file path")

    def handle(self, *args, **options):
        raise NotImplementedError()
