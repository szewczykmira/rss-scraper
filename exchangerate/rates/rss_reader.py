from datetime import datetime
from decimal import Decimal

import feedparser
from feedparser import FeedParserDict

FEED_URL = "https://www.ecb.europa.eu/rss/fxref-%s.html"


def get_data_from_rss_in_given_currency(currency: str) -> "FeedParserDict":
    """ Return all data for specified currency from RSS."""
    url = FEED_URL % currency
    feed = feedparser.parse(url)
    return feed.entries[0]


def validate_data(entry: "FeedParserDict"):
    if entry.cb_exchangerate is None or entry.updated is None:
        raise AttributeError("Feed does not contain required data")


def parse_data_from_entry(entry: "FeedParserDict") -> dict:
    """ Parse data from feed so that they could be processed in code."""
    validate_data(entry)
    description = entry.title or ""
    currency = entry.cb_targetcurrency.upper()
    exchange_rate, _ = entry.cb_exchangerate.split()
    update_date = datetime.fromisoformat(entry.updated)
    return {
        "description": description,
        "currency": currency,
        "exchange_rate": Decimal(exchange_rate),
        "parser_update_date": update_date,
    }


def get_data_for_currency(currency: str) -> dict:
    """ Fetch data from RSS and return them parsed."""
    feed_info = get_data_from_rss_in_given_currency(currency)
    return parse_data_from_entry(feed_info)
