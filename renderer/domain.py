from typing import Dict, List, Iterable

from pydantic import BaseModel


class ConfigResource(BaseModel):
    name: str
    template: str
    variables: Dict
    output_file: str

    @staticmethod
    def from_dict(resource):
        return ConfigResource(
            name=resource.get('name'),
            template=resource.get('template'),
            variables=resource.get('variables'),
            output_file=resource.get('output_file')
        )


class ConfigFile(BaseModel):
    resources: List[ConfigResource]

    @staticmethod
    def from_dict(dict_config):
        raw_resources = dict_config.get('resources')
        if not raw_resources:
            raise ValueError

        resources = [ConfigResource.from_dict(resource) for resource in raw_resources]
        if not resources:
            raise ValueError

        return ConfigFile(
            resources=resources
        )


class Template(BaseModel):
    raw_content: str
    rendered_content: str
    output_file: str

    @staticmethod
    def from_dict(item):
        return Template(
            raw_content=item.get('raw_content'),
            rendered_content=item.get('rendered_content'),
            output_file=item.get('output_file')
        )
