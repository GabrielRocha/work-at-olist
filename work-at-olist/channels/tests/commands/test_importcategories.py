from channels.management.commands import importcategories
from channels.models import Channel, Category
import argparse
import pytest


@pytest.fixture
def command():
    return importcategories.Command()


def test_add_arguments(command):
    parser = argparse.ArgumentParser()
    command.add_arguments(parser)
    args = parser.parse_args(["Walmart", "path"])
    assert args.channel == "Walmart"
    assert args.categories_file == "path"


@pytest.mark.django_db
@pytest.mark.django_db(transaction=True)
def test_handle_command(command):
    command.handle(categories_file='channels/tests/fixtures/categories.txt',
                   channel="Walmart")
    book_slug = "walmart-books-national-literature-science-fiction"
    computers_slug = "walmart-computers-tablets"
    assert Channel.objects.filter(name='Walmart').count() == 1
    assert Category.objects.count() == 23
    assert Category.objects.filter(slug=computers_slug).exists()
    assert Category.objects.filter(slug=book_slug).exists()


@pytest.mark.django_db
def test_importer_save_categories(channel):
    args = ['Computers',
            ['Computers\n', 'Computers / Notebooks\n'],
            channel]
    importcategories.save_categories(*args)
    assert Category.objects.filter(name="Computers").exists()
    parent = Category.objects.get(name="Computers")
    assert Category.objects.filter(name="Notebooks",
                                   parent=parent).exists()
