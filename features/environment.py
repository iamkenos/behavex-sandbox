import os
from dotenv import load_dotenv

def before_all(context):
    load_dotenv()

def before_feature(context, feature):
    feature.name = f"[{os.environ['BRAND']}] {feature.name}"
 