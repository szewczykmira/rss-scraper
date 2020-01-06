from datetime import timedelta

import pytest

from exchangerate.rates.exchange_rates import update_currency_data_from_rss
from exchangerate.rates.models import Rate
from exchangerate.rates.rss_reader import get_data_for_currency


def test_object_does_not_exists(db, mock_feed_return_value, feed_usd_data):
    assert not Rate.objects.exists()
    rate = update_currency_data_from_rss("USD", commit=True)
    assert rate.currency == "USD"
    assert rate.description == feed_usd_data.title
    assert Rate.objects.exists()


def test_feed_returns_empty_data(mock_feed_returns_attribute_error):
    with pytest.raises(AttributeError):
        update_currency_data_from_rss("USD")


def test_feed_returns_older_data_than_expected(mock_feed_return_value, rate):
    data_for_currency = get_data_for_currency("USD")
    rate_from_future = rate
    rate_from_future.parser_update_date += timedelta(days=4)
    rate.save()

    assert data_for_currency["parser_update_date"] < rate_from_future.parser_update_date
    old_exchange_rate = rate_from_future.exchange_rate
    old_update_date = rate_from_future.parser_update_date
    update_currency_data_from_rss("USD")
    rate_from_future.refresh_from_db()
    assert rate_from_future.parser_update_date == old_update_date
    assert rate_from_future.exchange_rate == old_exchange_rate


def test_rate_is_properly_updated(rate, mock_feed_return_value):
    data_for_currency = get_data_for_currency("USD")

    assert data_for_currency["parser_update_date"] > rate.parser_update_date
    old_exchange_rate = rate.exchange_rate
    old_update_date = rate.parser_update_date
    update_currency_data_from_rss("USD")
    rate.refresh_from_db()

    assert not rate.parser_update_date == old_update_date
    assert not rate.exchange_rate == old_exchange_rate
