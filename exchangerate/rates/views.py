from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Rate
from .serializers import RateSerializer


@api_view(["GET"])
def rates_list(request):
    """ Returns list of all rates."""
    rates = Rate.objects.all()
    serializer = RateSerializer(rates, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def rate_detail(request, currency):
    try:
        rate = Rate.objects.get(currency=currency.upper())
    except Rate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RateSerializer(rate)
    return Response(serializer.data)
