import pytest

from renderer.domain import ConfigFile
from renderer.usecases import render_config_from_file


@pytest.fixture()
def config_file(asset='assets/config.yaml') -> str:
    return asset


def test_usecase_can_generate_a_configfile_domain_object_when_config_is_ok(config_file):
    rendered_config = render_config_from_file(config_file)

    assert isinstance(rendered_config, ConfigFile)
