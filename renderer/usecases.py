import yaml
from jinja2 import Environment, StrictUndefined

from renderer.domain import ConfigFile, ConfigResource


def render_config_from_file(config_file: str) -> ConfigFile:
    with open(config_file, 'rb') as c:
        config = yaml.load(c.read(), yaml.SafeLoader)

    return ConfigFile.from_dict(config)


def render_template_from_config_resource(resource: ConfigResource) -> str:
    with open(resource.template, 'rb') as tfile:
        template = Environment(undefined=StrictUndefined).from_string(source=tfile.read().decode())

    return template.render(**resource.to_render)
