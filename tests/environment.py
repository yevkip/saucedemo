import os
import yaml
from tests.lib import get_app


def load_config():
    file_name = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(file_name) as input:
        return yaml.safe_load(input)


def before_all(context):
    context.config = load_config()


def before_scenario(context, scenario):
    context.app = get_app(context.config)


def after_scenario(context, scenario):
    context.app.shutdown()


def after_all(context):
    context.app.shutdown()
