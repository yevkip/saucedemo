import os
import yaml
from tests.lib import get_app


def load_config():
    file_name = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(file_name) as input:
        return yaml.safe_load(input)


def before_all(context):
    browser = context.config.userdata.get('browser')
    context.config = load_config()

    if browser:
        available_browsers = context.config['browsers'].keys()
        if browser not in available_browsers:
            raise ValueError(f'{browser} is not recognised. Available browsers {available_browsers}')
        context.browser = browser
    else:
        context.browser = 'CHROME-LOCAL'


def before_scenario(context, scenario):
    if 'skip' in scenario.tags:
        scenario.skip("Skipping this scenario")

    context.app = get_app(config=context.config,
                          browser_name=context.browser)


def after_scenario(context, scenario):
    context.app.shutdown()


def after_all(context):
    if getattr(context, "app", None):
        context.app.shutdown()
