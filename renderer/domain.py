from typing import Dict, List

from pydantic import BaseModel


class ConfigResource(BaseModel):
    name: str
    template: str
    variables: Dict

    @staticmethod
    def from_dict(resource):
        return ConfigResource(
            name=resource.get('name'),
            template=resource.get('template'),
            variables=resource.get('variables')
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
