from django.shortcuts import render
from .models import Restaurant, Rating,Sale
from django.db.models import Prefetch,Sum
from django.utils import timezone

# Create your views here.
from .forms import RatingForm


def index(request):
    # if request.method == "POST":
    #     form = RatingForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()

    #     else:
    #         return render(request, "index.html", {"form": form})
    # context = {"form": RatingForm()}
    # restaurants=Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings','sales')
    # context={'restaurants':restaurants}
    month_ago=timezone.now()-timezone.timedelta(days=30)
    monthly_sales=Prefetch('sales',queryset=Sale.objects.filter(datetime__gte=month_ago))
    # ratings = Rating.objects.only('rating','restaurant__name').select_related("restaurant")
    restaurants=Restaurant.objects.prefetch_related('ratings',monthly_sales).filter(ratings__rating=5)
    restaurants=restaurants.annotate(total=Sum('sales__income'))

    context = {"restaurants": restaurants}

    print([r.total for r in restaurants])
    return render(request, "index.html", context)
