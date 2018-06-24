#!/usr/bin/env python
import os
import re

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if __name__ == '__main__':

    cf_template_file = "%s/cloudformation/{{ cookiecutter.cloudformation_template_name }}.yml.tpl" % PROJECT_DIRECTORY
    cf_template_name = "{{ cookiecutter.cloudformation_template_name }}"
    cf_template_description = "{{ cookiecutter.cloudformation_template_description }}"
    cf_template_version = "{{ cookiecutter.version }}"

    r = re.compile(r"\%\%(\S+)\%\%")
    with open(cf_template_file, "r") as f:
        lines = f.readlines()

    with open(cf_template_file, "w") as f:
        for l in lines:
            m = r.search(l)
            if m:
                if m.group() == "%%cookiecutter.cloudformation_template_name%%":
                    _l = r.sub(cf_template_name, l)
                    f.write(_l)
                elif m.group() == "%%cookiecutter.cloudformation_template_description%%":
                    _l = r.sub(cf_template_description, l)
                    f.write(_l)
                elif m.group() == "%%cookiecutter.version%%":
                    _l = r.sub(cf_template_version, l)
                    f.write(_l)
            else:
                f.write(l)
