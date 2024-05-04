from rest_framework import filters

from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
)

from .serializers import (
    ApartmentListSerializer,
    ApartmentUpdateSerializer,
    ManagerCreateSerializer,
    ManagerListSerializer,
    ManagerUpdateSerializer,
)
from .models import (
    Apartment,
    Client,
    Manager,
)
from .filters import (
    ApartmentFilter
)


class ApartmentListView(ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    filterset_class = ApartmentFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ApartmentListSerializer
        elif self.request.method == 'POST':
            return ApartmentListSerializer


# судя по фигме при нажатии на кнопку "Изменить", мы не изменяем существующую модельку квартиры, а наоборот создаем
# новый объект клиента. Поэтому хоть и называется 'ApartmentUpdateView', на самом деле мы создаем нового клиента.
class ApartmentUpdateView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ApartmentUpdateSerializer


class ApartmentDeleteView(DestroyAPIView):
    queryset = Apartment
    serializer_class = ApartmentListSerializer


class ManagerListView(ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ManagerListSerializer
        elif self.request.method == 'POST':
            return ManagerCreateSerializer


class ManagerUpdateView(UpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializer


class ManagerDeleteView(DestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerCreateSerializer


