from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
          if not Product.objects.filter(title=request.POST['title']).exists():
            form.save()
            form = ProductForm()

    context = {
        'form': form
    }
    # query
    # obj = Product.objects.get(id = 3)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    objs = Product.objects.all()
    context = {
        'objs': objs
    }
    return render(request, 'products/product_detail.html', context)

def product_raw_create_view(request):
    context = {}
    return render(request, 'products/product_raw_create.html', context)