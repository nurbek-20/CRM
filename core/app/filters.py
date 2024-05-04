from django_filters import rest_framework as filters, ChoiceFilter
from .models import Apartment


class ApartmentFilter(filters.FilterSet):
    status = ChoiceFilter(
        field_name='client__status',
        choices=(
            ('active', 'Активно'),
            ('reserved', 'Бронь'),
            ('sold', 'Продано'),
            ('instalment', 'Рассрочка'),
            ('barter', 'Бартер'),
        )
    )

    class Meta:
        model = Apartment
        fields = ('status', )

