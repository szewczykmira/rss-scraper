from exchangerate.celery import app

from .exchange_rates import update_all_currencies


@app.task(name="update-exchange-rates")
def update_exchange_rates():
    update_all_currencies()
