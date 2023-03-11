"""
A wrapper class for the feed cache stored in DynamoDB
"""
import boto3
import settings as S


class FeedCache:
    """
    FeedCache class
    """

    def __init__(self):
        self._aws_access_key_id = S.AWS_ACCESS_KEY_ID
        self._aws_secret_access_key = S.AWS_ACCESS_KEY
        self._region_name = S.AWS_REGION

        self._ddb = boto3.resource(
            "dynamodb",
            aws_access_key_id=f"{self._aws_access_key_id}",
            aws_secret_access_key=f"{self._aws_secret_access_key}",
            region_name=f"{self._region_name}",
        )

    def scan(self):
        table = self._ddb.Table(f"{S.DYNAMO_DB_TABLE}")
        response = table.scan()
        print("The query returned the following items:")
        for item in response["Items"]:
            print(item)
