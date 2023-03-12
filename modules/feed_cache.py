"""
A wrapper class for the feed cache stored in DynamoDB
"""
import boto3
import settings as S
from botocore.exceptions import ClientError
from datetime import datetime
from .access_key import AccessKey


class FeedCache:
    """
    FeedCache class
    """

    def __init__(self):
        self._ddb = None
        self._table = None
        try:
            self._ddb = boto3.resource(
                "dynamodb",
                aws_access_key_id=AccessKey().decrypt(S.AWS_ACCESS_KEY_ID),
                aws_secret_access_key=AccessKey().decrypt(S.AWS_ACCESS_KEY),
                region_name=S.AWS_REGION,
            )
            self._table = self._ddb.Table(f"{S.DYNAMO_DB_TABLE}")
        except Exception as ex:
            print(ex)
            raise Exception(
                f"{datetime.now()}: Could not instantiate the FeedCache object."
            )

    @property
    def item_count(self):
        return self._table.item_count

    def all_scan(self):
        if self._table:
            try:
                response = self._table.scan()
                print("The query returned the following items:")
                for item in response["Items"]:
                    print(item)
            except Exception as ex:
                print(ex)
        else:
            raise Exception(
                f"{datetime.now()}: Cannot scan, the DynamoDB resource is invalid."
            )

    def get_item(self, p_key=None, s_key=None):
        item = None
        if p_key and s_key:
            response = self._table.get_item(
                Key={S.DYNAMO_P_KEY: p_key, S.DYNAMO_S_KEY: s_key}
            )
            item = response.get("Item")
        return item
