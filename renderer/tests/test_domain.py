import pytest
from typing import Dict
from yaml import load, SafeLoader as Loader

from renderer.domain import ConfigFile


@pytest.fixture()
def template_file(asset='assets/file.tmpl'):
    with open(asset, 'rb') as template:
        return template.read().decode()


@pytest.fixture()
def config_file(asset='assets/config.yaml') -> Dict:
    with open(asset, 'rb') as template:
        return load(template, Loader)


def test_can_convert_a_config_into_domain_object(config_file):
    number_of_resources = len(config_file.get('resources'))

    config = ConfigFile.from_dict(config_file)

    assert config
    assert isinstance(config, ConfigFile)
    assert len(config.resources) == number_of_resources
