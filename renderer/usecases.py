import yaml

from renderer.domain import ConfigFile


def render_config_from_file(config_file: str) -> ConfigFile:
    with open(config_file, 'rb') as c:
        config = yaml.load(c.read(), yaml.SafeLoader)

    return ConfigFile.from_dict(config)
