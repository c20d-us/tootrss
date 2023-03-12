"""
A wrapper class for an RSS feed
"""
import feedparser


class Feed:
    """
    Feed class
    """

    def __init__(self, feed_uri=None):
        self._data = None
        self._title = None
        self._items = {}
        try:
            self._data = feedparser.parse(feed_uri)
            self._title = self._data.feed.title
            self._load_items()
        except Exception as _ex:
            print(_ex)

    def _make_datestamp(self, date_tuple=None):
        d = "0" * 14
        if date_tuple:
            d = f"{date_tuple[0]:04}"
            for i in range(1, 6):
                d = "".join([d, f"{date_tuple[i]:02}"])
        return d

    def _load_items(self):
        if self._data:
            for entry in self._data.entries:
                item_key = "-".join(
                    [self._make_datestamp(entry.published_parsed), entry.id]
                )
                self._items[item_key] = {
                    "title": entry.title,
                    "link": entry.link,
                    "tooted": False,
                }

    @property
    def title(self):
        return self._title

    @property
    def items(self):
        return self._items

    @property
    def item_count(self):
        return len(self._items)
