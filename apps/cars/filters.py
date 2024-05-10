from django.db.models import QuerySet
from django.http import QueryDict
from apps.cars.models import CarsModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarsModel.objects.all()
    for key, value in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case 'price_gte':
                qs = qs.filter(price__gte=value)
            case 'price_lte':
                qs = qs.filter(price__lte=value)

            case 'year_gt':
                qs = qs.filter(year__gt=value)
            case 'year_lt':
                qs = qs.filter(year__lt=value)
            case 'year_gte':
                qs = qs.filter(year__gte=value)
            case 'year_lte':
                qs = qs.filter(year__lte=value)

            case 'v_gt':
                qs = qs.filter(year__gt=value)
            case 'v_lt':
                qs = qs.filter(price__lt=value)
            case 'v_gte':
                qs = qs.filter(price__gte=value)
            case 'v_lte':
                qs = qs.filter(price__lte=value)

            case 'brand_start':
                qs = qs.filter(brand__startswith=value)
            case 'brand_end':
                qs = qs.filter(brand__endswith=value)
            case 'brand_contains':
                qs = qs.filter(brand__contains=value)

            case 'body_start':
                qs = qs.filter(body__startswith=value)
            case 'body_end':
                qs = qs.filter(body__endswith=value)
            case 'body_contains':
                qs = qs.filter(body__contains=value)

    return qs
