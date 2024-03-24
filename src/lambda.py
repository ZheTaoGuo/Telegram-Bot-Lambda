import json
import logging
import os
import boto3
import dotenv

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.resource('dynamodb', region_name='ap-southeast-1')
table = client.Table('foot-pedal-data')
print('this is table', table)


def handler(event, context):
    try:
        logger.info(f"Lambda function ARN: {context.invoked_function_arn}")
        logger.info(f"CloudWatch log stream name: {context.log_stream_name}")
        logger.info(f"CloudWatch log group name: {context.log_group_name}")
        logger.info(f"Lambda Request ID: {context.aws_request_id}")
        logger.info(
            f"Lambda function memory limits in MB: {context.memory_limit_in_mb}"
        )
        logger.info("## ENVIRONMENT VARIABLES")
        logger.info(os.environ["AWS_LAMBDA_LOG_GROUP_NAME"])
        logger.info(os.environ["AWS_LAMBDA_LOG_STREAM_NAME"])
        logger.info(os.environ["AWS_REGION"])
        logger.info("## EVENT")
        logger.info(event)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(event),
        }
    except Exception as e:
        logger.error(e)
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"Error": str(e)}),
        }
