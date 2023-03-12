"""
A wrapper class for the feed cache stored in DynamoDB
"""
import boto3
import settings as S
from datetime import datetime
from .access_key import AccessKey


class FeedCache:
    """
    FeedCache class
    """
    def __init__(self):
        self._ddb = None
        try:
            aws_access_key = AccessKey().decrypt(S.AWS_ACCESS_KEY)
            aws_access_key_id = AccessKey().decrypt(S.AWS_ACCESS_KEY_ID)
            self._ddb = boto3.resource(
                "dynamodb",
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_access_key,
            )
        except Exception as ex:
            print(ex)
            raise Exception(f"{datetime.now()}: Could not instantiate the FeedCache object.")

    def all_scan(self):
        if self._ddb:
            table = self._ddb.Table(f"{S.DYNAMO_DB_TABLE}")
            try:
                response = table.scan()
                print("The query returned the following items:")
                for item in response["Items"]:
                    print(item)
            except Exception as ex:
                print(ex)
        else:
           raise Exception(f"{datetime.now()}: The DynamoDB resource is invalid.")