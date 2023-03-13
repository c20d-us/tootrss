"""
A wrapper class for an RSS feed
"""
import feedparser


class Feed:
    """
    Feed class
    """

    def __init__(self, feed_uri: str = None) -> None:
        self._items = {}
        self._title = None
        self._data = feedparser.parse(feed_uri)
        if not self._data.bozo:
            self._title = self._data.feed.title
            self._load_items()
        else:
            raise Exception(f"Could not parse the feed '{feed_uri}'")

    def _make_datestamp(self, date_tuple: tuple = None) -> str:
        d = "0" * 14
        if date_tuple:
            d = f"{date_tuple[0]:04}"
            for i in range(1, 6):
                d = "".join([d, f"{date_tuple[i]:02}"])
        return d

    def _load_items(self) -> bool:
        loaded = False
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
            loaded = True
        return loaded

    @property
    def title(self) -> str:
        return self._title

    @property
    def items(self) -> dict:
        return self._items

    @property
    def item_count(self) -> int:
        return len(self._items)
