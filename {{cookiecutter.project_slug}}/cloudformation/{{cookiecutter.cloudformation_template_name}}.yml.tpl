{% macro include(file) %}{% include(file) %}{% endmacro %}

AWSTemplateFormatVersion: "2010-09-09"
Description: %%cookiecutter.cloudformation_template_description%%
Metadata:
  TemplateVersion: %%cookiecutter.version%%
Parameters:
  {{ include("parameters/%%cookiecutter.cloudformation_template_name%%.yml")|indent(2) }}
Mappings:
  {{ include("mappings/%%cookiecutter.cloudformation_template_name%%.yml")|indent(2) }}
Resources:
  {{ include("resources/%%cookiecutter.cloudformation_template_name%%_iam.yml")|indent(2) }}
  {{ include("resources/%%cookiecutter.cloudformation_template_name%%_sg.yml")|indent(2) }}
  {{ include("resources/%%cookiecutter.cloudformation_template_name%%_lambda.yml")|indent(2) }}
  {{ include("resources/%%cookiecutter.cloudformation_template_name%%_trigger.yml")|indent(2) }}
Outputs:
  {{ include("%%cookiecutter.cloudformation_template_name%%_output.yml")|indent(2) }}
