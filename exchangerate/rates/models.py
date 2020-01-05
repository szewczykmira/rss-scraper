from django.db import models


class Rate(models.Model):
    currency_name = models.CharField(max_length=3, unique=True)
    exchange_rate = models.DecimalField(decimal_places=4, max_digits=50)
    parser_update_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.description
