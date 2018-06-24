# Update this to give whichever name you want. This may be set on the command line:
# > make build OUT_FILE=./outfile.zip
OUT_FILE?=./{{cookiecutter.aws_lambda_package_name}}.zip

### Below this point it should not need to be changed
# get absolute path of zipfile to deliver
DELIVERABLE=$(abspath $(OUT_FILE))

# Install all the libs locally
install:
	pipenv sync -d

# Destroy the virtualenv
uninstall:
	pipenv --rm

# Run the import
run:
	pipenv run python ./{{cookiecutter.aws_lambda_entry_filename}}.py

# Clean delivrable
clean:
	rm -f ${DELIVERABLE}

# Rebuild the delivrable
build:
	$(eval VENV = $(shell pipenv --venv))
	cd ${VENV}/lib/python3.6/site-packages && zip -r9 ${DELIVERABLE} ./*
	zip -r9 ${DELIVERABLE} *.py
	cd cloudformation && jinja2 {{cookiecutter.cloudformation_template_name}}.yml.tpl > {{cookiecutter.cloudformation_template_name}}.yml
