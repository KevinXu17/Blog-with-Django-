from django.shortcuts import render, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
              if not Product.objects.filter(title=request.POST.get('title')).exists():
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
    # if request.method == 'POST':
    #     new_title = request.POST.get("new_title")
    #     print("====", new_title)
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
        # else:
        #     print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'products/product_raw_create.html', context)

def render_initial_data(request):
    initial_data = {
        'title': 'This is the initial title'
    }
    form = RawProductForm(request.POST or None, initial=initial_data )
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id = my_id)
    context = {
        "obj": obj
    }
    return render(request, 'products/product_detail.html', context)