#!/usr/bin/env python3
"""
The Toot RSS client
"""
import json
import settings as S
from modules.feed_cache import FeedCache
from modules.rss_feed import Feed

# mastodon_access_token = AccessKey(S.MASTODON_ACCESS_TOKEN).decrypt()

# try:
#    fc = FeedCache()
#    fc.all_scan()
# except Exception as ex:
#    print(ex)

feed = Feed(S.FEED_URI)
print(f"{feed.title} has {feed.item_count} items")

print(json.dumps(feed.items, indent=4))
