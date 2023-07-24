from django.shortcuts import render

# from apps.models import Product, Category
from models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        search = data.get('search')
        from_price = data.get('from_price')
        to_price = data.get('to_price')
        from_date = data.get('from_date')
        to_date = data.get('to_date')
        categories_list = data.getlist('category')
        if search:
            products = products.filter(title__icontains=search)
        if categories_list:
            products = products.filter(categories__id__in=categories_list)
        if from_price or to_price:
            products = products.filter(price__range=[from_price, to_price])
        if from_date or to_date:
            products = products.filter(created_at__range=[from_date, to_date])
    count = products.count()
    return render(request, 'index.html',
                  {'products': products[:8], 'categories': categories, 'count': count})
