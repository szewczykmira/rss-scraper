from datetime import timedelta
from decimal import Decimal

import pytest
from django.utils import timezone
from feedparser import FeedParserDict

from exchangerate.rates import exchange_rates, rss_reader
from exchangerate.rates.models import Rate


@pytest.fixture
def feed_usd_data():
    return FeedParserDict(
        title="Test description",
        cb_targetcurrency="USD",
        cb_exchangerate="12\nEUR",
        updated=timezone.now().isoformat(),
    )


@pytest.fixture
def mock_feed_return_value(monkeypatch, feed_usd_data):
    monkeypatch.setattr(
        rss_reader, "get_data_from_rss_in_given_currency", lambda x: feed_usd_data,
    )


@pytest.fixture
def mock_feed_returns_attribute_error(monkeypatch):
    def mock_function(*args):
        raise AttributeError("Not enough value")

    monkeypatch.setattr(
        exchange_rates, "get_data_for_currency", mock_function,
    )


@pytest.fixture
def rate(db):
    return Rate.objects.create(
        description="Test description",
        currency="USD",
        exchange_rate=Decimal("1.200"),
        parser_update_date=timezone.now() - timedelta(days=1),
    )
