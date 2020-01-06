import pytest
from feedparser import FeedParserDict


@pytest.fixture
def parser_usd_data():
    return FeedParserDict(
        title="Test description",
        cb_targetcurrency="USD",
        cb_exchangerate="12\nEUR",
        updated="2019-12-27T14:15:00+01:00",
    )
