#!/usr/bin/env python3
"""
The Toot RSS client
"""
import settings as S
from modules.feed_cache import FeedCache

# mastodon_access_token = AccessKey(S.MASTODON_ACCESS_TOKEN).decrypt()

try:
    fc = FeedCache()
    fc.all_scan()
except Exception as ex:
    print(ex)
