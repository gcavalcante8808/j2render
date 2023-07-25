from typing import Iterable, List

import yaml
from jinja2 import Environment, StrictUndefined

from renderer.domain import ConfigFile, ConfigResource, Template


def persist_rendered_templates_on_local_filesystem(templates: Iterable[Template]) -> None:
    for template in templates:
        with open(template.output_file, 'wb') as tfile:
            tfile.write(template.rendered_content.encode())


def render_templates_from_configfile(config_file) -> Iterable[Template]:
    config = render_config_from_file(config_file)

    return (render_template_from_config_resource(resource) for resource in config.resources)


def render_config_from_file(config_file: str) -> ConfigFile:
    with open(config_file, 'rb') as c:
        config = yaml.load(c.read(), yaml.SafeLoader)

    return ConfigFile.from_dict(config)


def render_template_from_config_resource(resource: ConfigResource) -> Template:
    with open(resource.template, 'rb') as tfile:
        raw_content = tfile.read().decode()
        template = Environment(undefined=StrictUndefined).from_string(source=raw_content)

    return Template.from_dict({
        'raw_content': raw_content,
        'rendered_content': template.render(**resource.variables),
        'output_file': resource.output_file
    })
