from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

import feedparser

if TYPE_CHECKING:
    from feedparser import FeedParserDict

FEED_URL = "https://www.ecb.europa.eu/rss/fxref-%s.html"


def get_data_from_rss_in_given_currency(currency: str) -> "FeedParserDict":
    """ Return all data for specified currency from RSS."""
    url = FEED_URL % currency
    feed = feedparser.parse(url)
    return feed[0]


def parse_data_from_entry(entry: "FeedParserDict") -> dict:
    """ Parse data from feed so that they could be processed in code."""
    description = entry.title
    currency = entry.cb_targetcurrency.upper()
    exchange_rate, _ = entry.cb_exchangerate.split()
    update_date = datetime.fromisoformat(entry.updated)
    return {
        "description": description,
        "currency": currency,
        "exchange_rate": Decimal(exchange_rate),
        "parser_update_date": update_date,
    }
