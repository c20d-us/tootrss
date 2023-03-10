"""
These settings are common to all environments unless overriden
"""
AWS_ACCESS_KEY_ID = "xxxx"
AWS_ACCESS_KEY = "xxxx"
AWS_REGION = "us-west-2"

DYNAMO_DB_TABLE = "c20d-blog-feed-cache"
DYNAMO_P_KEY = "feed-title"
DYNAMO_S_KEY = "item-guid"

FEED_URI = "https://c20d.blog/index.xml"

MASTODON_ACCESS_TOKEN = "xxxx"
MASTODON_INSTANCE_URI = "https://hachyderm.io"
MASTODON_STATUS_ENDPOINT = "/api/v1/statuses"
MASTODON_STATUS_METHOD = "post"
MASTODON_STATUS_VISIBILITY = "direct"