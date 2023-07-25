import pytest
import yaml

from renderer.domain import ConfigFile, Template
from renderer.usecases import render_config_from_file, render_template_from_config_resource, \
    render_templates_from_configfile, persist_rendered_templates_on_local_filesystem


@pytest.fixture()
def config_file(asset='assets/config.yaml') -> str:
    return asset


def test_generate_a_configfile_domain_object_when_config_is_ok(config_file):
    rendered_config = render_config_from_file(config_file)

    assert isinstance(rendered_config, ConfigFile)


def test_can_render_a_single_resource_when_config_is_ok(config_file):
    config = render_config_from_file(config_file)

    template = render_template_from_config_resource(config.resources[0])

    assert isinstance(template, Template)
    parsed_template = yaml.load(template.rendered_content, Loader=yaml.SafeLoader)
    assert parsed_template['items'][0]['key1'] == config.resources[0].variables['key1']
    assert parsed_template['items'][1]['key2'] == config.resources[0].variables['key2']
    assert parsed_template['items'][2]['key3'] == config.resources[0].variables['key3']


def test_render_templates_from_configfile_when_config_is_oks(config_file):
    config = render_config_from_file(config_file)

    templates = list(render_templates_from_configfile(config_file))

    parsed_templates = [yaml.load(template.rendered_content, Loader=yaml.SafeLoader) for template in templates]
    assert len(parsed_templates) == len(config.resources)
    assert parsed_templates[0]['items'][0]['key1'] == config.resources[0].variables['key1']
    assert parsed_templates[1]['items'][0]['key1'] == config.resources[1].variables['key1']
    assert parsed_templates[2]['this']['is']['a']['template']['with']['values'][0]['key1'] == config.resources[2].variables['key1']


def teste_render_and_persist_templates_on_localfilesystem_when_config_is_ok(config_file):
    config = render_config_from_file(config_file)
    expected_files = [resource.output_file for resource in config.resources]
    templates = render_templates_from_configfile(config_file)

    persisted_files = persist_rendered_templates_on_local_filesystem(templates)

    assert persisted_files == expected_files
