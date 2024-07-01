from testapp.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint


def run():

    # restaurant=Restaurant()
    # restaurant.name="My Italian Restaurant"
    # restaurant.latitude=50.2
    # restaurant.longitude=50.2
    # restaurant.date_opened=timezone.now()
    # restaurant.restaurant_type=Restaurant.TypeChoices.ITALIAN
    # restaurant.save()
    # print(Restaurant.objects.all())
    # restaurant=Restaurant.objects.first()
    # restaurant=Restaurant.objects.all()[0]
    # print(restaurant)
    # Restaurant.objects.create(
    #     name='Pizza shop',
    #     date_opened=timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN,
    #     latitude=43,
    #     longitude=43
    # )
    # restaurant=Restaurant.objects.first()
    # user=User.objects.first()
    # Rating.objects.create(user=user,restaurant=restaurant,rating=4)

    # rating=Rating.objects.first()
    # print(rating.restaurant.name)

    # restaurant=Restaurant.objects.first()
    # print(restaurant.rating_set.all())
    # print(restaurant.ratings.all())

    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=2.33,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=3.33,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=4.33,
    #     datetime=timezone.now()
    # )

    # user=User.objects.first()
    # restaurant=Restaurant.objects.first()
    # print(
    #     Rating.objects.get_or_create(
    #         restaurant=restaurant,
    #         user=user,
    #         rating=4
    #     )
    # )
    # rating=Rating(user=user,restaurant=restaurant,rating=9)
    # rating.full_clean()
    # rating.save()

    # restaurant=Restaurant.objects.first()
    # restaurant.name='Chla jaa yaha s'
    # restaurant.save(update_fields=['name'])

    # restaurant=Restaurant()
    # restaurant.name='Meri dukaan'
    # restaurant.restaurant_type=Restaurant.TypeChoices.INDIAN
    # restaurant.date_opened=timezone.now()
    # restaurant.latitude=40
    # restaurant.longitude=50
    # restaurant.save()

    # restaurant=Restaurant.objects.all()

    # restaurant.update(
    #     date_opened=timezone.now()
    # )

    # restaurant=Restaurant.objects.filter(name__startswith='M')
    # print(restaurant)

    # for i in restaurant:
    #     i.name+='and Indian'

    # for i in restaurant:
    #     i.save()

    # restaurant=Restaurant.objects.first()
    # restaurant.delete()

    # restaurant=Restaurant.objects.filter(name='abhi khula nhi h')
    # print(restaurant.exists())

    # chinese=Restaurant.TypeChoices.CHINESE
    # indian=Restaurant.TypeChoices.INDIAN
    # mexican=Restaurant.TypeChoices.MEXICAN
    # restaurant=Restaurant.objects.filter(restaurant_type__in=[chinese,indian,mexican])
    # print(restaurant)
    # restaurant=Restaurant.objects.exclude(restaurant_type=chinese)
    # print(restaurant)

    #  Optimiazation queries



    pprint(connection.queries)
    print("Successs")
