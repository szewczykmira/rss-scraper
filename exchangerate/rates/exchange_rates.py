from django.core.exceptions import ObjectDoesNotExist

from .models import Rate
from .rss_reader import get_data_for_currency


def update_currency_data_from_rss(currency: str, commit: bool = True) -> Rate:
    """ Fetch data from RSS feed.
    If feed for given currency does not exists - create it.
    If saved feed is older than fetched one - update db.
    """
    currency_data = get_data_for_currency(currency)

    try:
        current_rate = Rate.objects.get(currency=currency)
    except ObjectDoesNotExist:
        current_rate = Rate(**currency_data)
    else:
        new_update_date = currency_data["parser_update_date"]
        if current_rate.parser_update_date < new_update_date:
            current_rate.parser_update_date = new_update_date
            current_rate.exchange_rate = currency_data["exchange_rate"]
            current_rate.description = currency_data["description"]

    if commit:
        current_rate.save()
    return current_rate
