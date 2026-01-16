import os
from dotenv import load_dotenv

def before_all(context):
    load_dotenv()

def before_feature(context, feature):
    # sample snippet on how to mutate feature name via before_feature hook
    # prefixes feature name with the env BRAND value, helps with identifiying what
    # BRAND a test run is for in the html report that's generated
    feature.name = f"[{os.environ['BRAND']}] {feature.name}" 

def before_scenario(context, scenario):
    pass

def before_step(context, step):
    pass


def after_step(context, step):
    pass

def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass 
 
def after_all(context):
    pass