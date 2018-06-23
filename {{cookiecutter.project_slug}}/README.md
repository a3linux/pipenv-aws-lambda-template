# {{cookiecutter.project_name}}

Minimal project to get up and running on AWS lambda with Python 3.6 and [pipenv](http://docs.pipenv.org/).

## Quickstart

The main commands are wrapped using a very simple Makefile.
It should be working for Linux/macOS _ONLY_.

### Install

The first time only:
- `make install`: Create a virtual environment and install dependencies using pipenv

### Test locally

- `make run`: call the lambda handler using `pipenv run`

### Build

- `make build`: Collect dependencies and entry point script into a
  [deployment package](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)

  By default, it'll be a `{{cookiecutter.aws_lambda_package_name}}.zip` in the root of the project.

  The target is customisable and may be provided on the command line:

      make build OUT_FILE=outfile.zip

### Upload and Deploy

- Go to your AWS account, in the "Lambda" section
- Click "Create a function" > "Author from scratch" > Configure triggers page: Click "Next"
- Give a name & description, choose Python 3.6 runtime
- Select "Upload a ZIP file" and choose the delivrable in the file picker
- Set the Handler to `{{cookiecutter.aws_lambda_entry_filename}}.{{cookiecutter.aws_lambda_entry}}` (or more generally <script_name>.<function_name>)
- Select/create an AWS Role, click "Next"
- Review all the details and confirm creation
- Run it!

### Next steps

- Add any third party package you might need using `pipenv install ...`
- To deploy, run the build script and re-upload the ZIP file
- Settings can be added as environment variables in AWS
- Triggers can be configured to run your function: API gateway, Alexa, Cloudwatch, SNS, ...
