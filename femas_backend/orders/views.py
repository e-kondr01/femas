from .models import *
from .serializers import *
from .utils import CreateRetrieveAPIView


class CreateOrderView(CreateRetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    retrieve_serializer_class = RetrieveOrderSerializer
