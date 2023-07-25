import pytest
import yaml

from renderer.domain import ConfigFile
from renderer.usecases import render_config_from_file, render_template_from_config_resource


@pytest.fixture()
def config_file(asset='assets/config.yaml') -> str:
    return asset


def test_usecase_can_generate_a_configfile_domain_object_when_config_is_ok(config_file):
    rendered_config = render_config_from_file(config_file)

    assert isinstance(rendered_config, ConfigFile)


def test_usecase_can_render_a_single_resource_when_config_is_ok(config_file):
    config = render_config_from_file(config_file)

    template = render_template_from_config_resource(config.resources[0])

    assert template
    parsed_template = yaml.load(template, Loader=yaml.SafeLoader)
    assert parsed_template['items'][0]['key1'] == config.resources[0].to_render['key1']
    assert parsed_template['items'][1]['key2'] == config.resources[0].to_render['key2']
    assert parsed_template['items'][2]['key3'] == config.resources[0].to_render['key3']
