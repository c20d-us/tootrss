"""
A wrapper class for the feed cache stored in DynamoDB
"""
import boto3
from .encrypted_token import EncryptedToken


class FeedCache:
    """
    A class to manage the RSS feed cache stored in AWS DynamoDB

    Parameters
    ----------
    access_key_id: str
        The AWS access key ID
    access_key: str
        The AWS secret access key
    region: str
        The AWS region of the DynamoDB, i.e., "us-west-2"
    table_name: str
        The name of the DynamoDB table to use
    p_key_name: str
        The name of the table's partition key
    s_key_name: str
        The name of the table's sort key

    Methods
    -------
    get_all()
        Retrieves all record items from the DynamoDB
    get_item()
        Retrieves a single item record from the DynamoDB
    put_item()
        Puts an item into the DynamoDb (overwrites if already present)
    """

    def __init__(self, access_key_id: str, access_key: str, region: str, table_name: str, p_key_name: str, s_key_name: str) -> None:
        """
        The initializer

        Raises
        ------
        Exception:
            If the Fernet key is not valid, a generic Exception is raised
        """
        self._table = None
        self._p_key_name = p_key_name
        self._s_key_name = s_key_name
        try:
            ddb = boto3.resource(
                "dynamodb",
                aws_access_key_id=access_key_id,
                aws_secret_access_key=access_key,
                region_name=region,
            )
            self._table = ddb.Table(table_name)
        except Exception as ex:
            print(ex)
            raise Exception(
                f"Could not instantiate the FeedCache object."
            )

    def get_all(self) -> list[dict]:
        """
        Scan the entire DynamoDB cache and return all records.
        
        Parameters
        ----------
        None

        Returns
        -------
        list[dict]: A list of item dictionaries from the cache DB

        Raises
        ------
        Exception
            If the table can't be scanned, raises a generic Exception
        """
        items = None
        try:
            response = self._table.scan()
            items = response["Items"]
        except Exception as ex:
            raise Exception(f"get_all encountered exception {ex}")
        return items

    def get_item(self, p_key: str, s_key: str) -> dict:
        """
        Get a single item from the DynamoDC cache, if it exists
        
        Parameters
        ----------
        p_key: str
            The value for the DynamoDB partition key
        s_key: str
            The value for the DynamoDB sort key

        Returns
        -------
        dict: An item dictionary

        Raises
        ------
        Exception
            If the get action fails, raises a generic Exception
        """
        item = None
        try:
            response = self._table.get_item(
                Key={self._p_key_name: p_key, self._s_key_name: s_key}
            )
            item = response.get("Item")
        except Exception as ex:
            raise Exception(f"get_item encountered exception {ex}")
        return item

    def put_item(self, p_key: str, s_key: str, link: str, title: str, tooted: bool) -> bool:
        """
        Put a single item into the DynamoDC cache
        
        Parameters
        ----------
        p_key: str
            The value for the DynamoDB partition key
        s_key: str
            The value for the DynamoDB sort key
        link: str
            The item link
        title: str
            The item title
        tooted: bool
            Whether the item has been tooted

        Returns
        -------
        bool: Whether the put_item action succeeded

        Raises
        ------
        Exception
            If the put_item action fails, raises a generic Exception
        """
        put_success = False
        try:
            response = self._table.put_item(
                Item={
                    self._p_key_name: p_key,
                    self._s_key_name: s_key,
                    'link': link,
                    'title': title,
                    'tooted': tooted
                }
            )
        except:
            raise Exception("Problem!")
        return put_success