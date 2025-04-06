#!/usr/bin/env python3.11
"""
Generates and writea a JSON Schema fragment for the fields
defined in hms.core.data_objects.BaseDataObject. That
document is for reference purposes only, but may be of
use for new engineers on the project, or for other teams'
reference.
"""

# Built-In Imports
from pathlib import Path

# Third-Party Imports
import yaml

from pydantic import BaseModel

# Path Manipulations (avoid these!) and "Local" Imports
from hms.core.data_objects import BaseDataObject

# Module "Constants" and Other Attributes
schema_yaml = Path(__file__).parent.parent \
    / 'documentation' / 'BaseDataObject-schema.yaml'

# Main Process
print(
    f'Writing the schema for {BaseDataObject} '
    f'to {schema_yaml}:'
)

# Since BaseDataObject is not, itself, a BaseModel
# with the model_json_schema method, create a class
# that inherits from BaseModel and BaseDataObject
# both in order to get that schema.
class BaseDataObjectForSchema(BaseModel, BaseDataObject):
    pass

schema = BaseDataObjectForSchema.model_json_schema()
output = {
    'title': 'BaseDataObject-schema-members',
    'description': 'The JSON schema definitions for '
    'the common fields provided by BaseDataObject, '
    'for reference purposes. See also the base-'
    'business-object.sql file in database/examples '
    'for the corresponding SQL implementation.',
    'properties': schema.get('properties', {})
}
schema_yaml.write_text(yaml.dump(output))
