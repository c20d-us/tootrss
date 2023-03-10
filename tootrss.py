#!/usr/bin/env python3
"""
The Toot RSS client
"""
import settings as S
from modules.feed_cache import FeedCache

print(f"Value: {S.FEED_URI}")

fc = FeedCache()

fc.scan()
