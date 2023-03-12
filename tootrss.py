#!/usr/bin/env python3
"""
The Toot RSS client
"""
import json
import settings as S
from modules.feed_cache import FeedCache
from modules.rss_feed import Feed


try:
    fc = FeedCache()
    # fc.all_scan()
    # print(f"Feed cache item count: {fc.item_count}")
    feed = Feed(S.FEED_URI)
    for item in sorted(feed.items):
        print(f"trying {item}")
        print(fc.get_item(feed.title, item))
except Exception as ex:
    print(ex)
