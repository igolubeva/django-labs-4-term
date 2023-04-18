from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from orders.serializers import OrderSerializer
from orders.models import Order
from orders.utils import send_report


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False)
    def send_report(self, request):
        send_report()
        return Response(status=status.HTTP_200_OK)
