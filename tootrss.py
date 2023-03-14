#!/usr/bin/env python3
"""
The Toot RSS client
"""
import json
import settings as S
from datetime import datetime
from mastodon import Mastodon
from modules.encrypted_token import EncryptedToken
from modules.feed_cache import FeedCache
from modules.rss_feed import Feed

C = None
F = None
M = None

def status_post(feed_title: str, item_title: str, link: str) -> None:
    post_message = (
        f"I just published a new post on {feed_title}. Check it out!\n\n"
        f"\"{item_title}\"\n"
        f"{link}"
    )
    M.status_post(
        post_message,
        visibility=S.MASTODON_STATUS_VISIBILITY
    )

def post_and_put(feed: Feed, item_key: str) -> None:
    status_post(feed.title, feed.items[item_key]['title'], feed.items[item_key]['link'])
    C.put_item(
        p_key=feed.title,
        s_key=item_key,
        link=feed.items[item_key]['link'],
        title=feed.items[item_key]['title'],
        tooted=True
    )

if __name__ == "__main__":
    try:
        C = FeedCache(
            access_key_id=EncryptedToken(S.FERNET_KEY, S.AWS_ACCESS_KEY_ID).decrypt(),
            access_key=EncryptedToken(S.FERNET_KEY, S.AWS_ACCESS_KEY).decrypt(),
            region=S.AWS_REGION,
            table_name=S.DYNAMO_DB_TABLE,
            p_key_name=S.DYNAMO_DB_P_KEY_NAME,
            s_key_name=S.DYNAMO_DB_S_KEY_NAME
        )
        F = Feed(S.FEED_URI)
        M = Mastodon(
            access_token = EncryptedToken(S.FERNET_KEY, S.MASTODON_ACCESS_TOKEN).decrypt(),
            api_base_url=S.MASTODON_BASE_URL
        )
        for item_key in sorted(F.items):
            cache_record = C.get_item(F.title, item_key)
            if not cache_record:
                post_and_put(F, item_key)
                break
            if cache_record and not cache_record['tooted']:
                post_and_put(F, item_key)
    except Exception as ex:
        print(ex)