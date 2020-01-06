from datetime import datetime
from decimal import Decimal

from exchangerate.rates.rss_reader import parse_data_from_entry


def test_data_from_entry_are_parsed_properly(feed_usd_data):
    usd_rate = parse_data_from_entry(feed_usd_data)
    assert usd_rate["currency"] == feed_usd_data.cb_targetcurrency.upper()
    assert usd_rate["description"] == feed_usd_data.title

    expected_rate = Decimal(feed_usd_data.cb_exchangerate.split()[0])
    assert usd_rate["exchange_rate"] == expected_rate

    expected_update_date = datetime.fromisoformat(feed_usd_data.updated)
    assert usd_rate["parser_update_date"] == expected_update_date
