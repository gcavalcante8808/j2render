from argparse import ArgumentParser


from renderer.usecases import render_templates_from_configfile, persist_rendered_templates_on_local_filesystem

parser = ArgumentParser()
parser.add_argument('-c', '--config', required=True)

args = parser.parse_args()

templates = render_templates_from_configfile(args.config)
persist_rendered_templates_on_local_filesystem(templates)
