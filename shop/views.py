from django.shortcuts import render, redirect
from .models import Product
from .forms import CategoryForm, ProductForm


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products_view.html', {'products': products})


def product_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_view.html', {'product': product})


def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_view')
    else:
        form = CategoryForm()
    return render(request, 'category_add_view.html', {'form': form})


def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_view')
    else:
        form = ProductForm()
    return render(request, 'product_add_view.html', {'form': form})
