# coding=utf-8

import settings
import utils
import feedparser
import aiohttp
import functools
from concurrent.futures import ALL_COMPLETED


class RssFluxUpdater:

    # region Ctor
    def __init__(self, limit=3, *args, **kwargs):
        self.limit = limit
        self.base_url = settings.RSS_FLUX
    # endregion

    # region Methods
    def fetch(self):
        response = feedparser.parse(self.base_url)
        result = [x.title for x in response['entries'][:self.limit]]
        return result
    # endregion
