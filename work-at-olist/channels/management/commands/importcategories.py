from itertools import groupby
from django.core.management.base import BaseCommand
from channels.models import Channel, Category
import pathos.multiprocessing as mp
from django.db import connection


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('channel', type=str, help="Channel name")
        parser.add_argument('categories_file', type=str, help="Categories file path")

    def handle(self, *args, **options):
        channel, _ = Channel.objects.get_or_create(name=options['channel'])
        channel.categories.all().delete()
        connection.close()
        with open(options['categories_file']) as categories:
            raws = categories.readlines()
            args = ((category.strip(), list(groups), channel)
                    for category, groups in groupby(raws, lambda x: x.split("/")[0].strip()))
        with mp.Pool() as pool:
            pool.starmap(save_categories, args)


def save_categories(category, groups, channel):
    first_level_category = Category.objects.create(channel=channel, name=category, parent=None)
    category_objects = {category: first_level_category}
    for group in list(groups)[1:]:
        categories = group.split("/")
        category = categories[-1].strip()
        parent = category_objects["/".join(categories[:-1]).strip()]
        category_objects["/".join(categories).strip()] = Category.objects.create(
            channel=channel, name=category, parent=parent)
