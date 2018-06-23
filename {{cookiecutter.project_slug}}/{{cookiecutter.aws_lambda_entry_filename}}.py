#!/usr/bin/env python
# -*- coding: utf-8 -*-

def {{cookiecutter.aws_lambda_entry}}(json_input, context):
    """TODO: Add your own logical of lambda_handler
    json_input - Lambda json input
    context - Lambda context input
    """
    print(json_input)
    print(context)
    print("This is AWS Lambda run by Python")


if __name__ == "__main__":
    print("Local run/test AWS Lambda Hanlder:")
    {{cookiecutter.aws_lambda_entry}}({}, None)
