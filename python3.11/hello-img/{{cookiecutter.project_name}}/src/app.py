import json

import mylogger

logger = mylogger.setup_logger(__name__)


def lambda_handler(event, context):
    logger.debug("done")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
