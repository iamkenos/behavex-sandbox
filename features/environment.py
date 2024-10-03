import os
from dotenv import load_dotenv

def before_all(context):
    load_dotenv()

def before_feature(context, feature):
    feature.name = f"[{os.environ['BRAND']}] {feature.name}"

def after_scenario(context, feature):
    data_id = 'PULLED_FROM_SOMEWHERE'
    context.scenario.name = f'{context.scenario.name}: {data_id}'

    if ('@1.1' in context.scenario.name):
        raise AssertionError
