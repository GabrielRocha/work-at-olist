from channels.management.commands import importcategories
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
