#!/usr/bin/env python3
from aws_cdk import Environment
from aws_cdk import App
from s3_stack.o2_arena_cdk_s3_stack import O2ArenaS3Stack
from lambda_firehose_stack.o2_arena_cdk_lambda_firehose_stack import O2ArenaLambdaFirehoseStack

""" Config settings:
    The hard-coded values can be input parameters or pulled from config files,
    once the code is released to production.
"""
input_params = dict([
    ('aws_account_id','143176219551'),
    ('aws_region', 'eu-west-1'),
    ('db_secret_arn_nosuffix','arn:aws:secretsmanager:eu-west-1:143176219551:secret:prod/db/mysql-onprem-o2arena-db-x'),
    ('vpc_id', 'vpc-74c9310d'),
    ('subnet', 'subnet-f7f1f4bf'),
    ('sg', 'sg-0f192c4f4b4ea7351')
  ])

# AWS Settings
app = App()
env_ireland = Environment(account=input_params['aws_account_id'], region=input_params['aws_region'])

# Stacks definition
s3_stack = O2ArenaS3Stack(app, "o2-arena-s3-stack", 
                                input_metadata=input_params, 
                                env=env_ireland)

lambda_firehose_stack = O2ArenaLambdaFirehoseStack(app, "o2-arena-lambda-firehose-stack", 
                                input_metadata=input_params,
                                input_s3_bucket_arn=s3_stack.bucket.bucket_arn,
                                env=env_ireland)

app.synth()
