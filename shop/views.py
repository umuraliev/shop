from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import ProductForm


def get_product_list(request, category_slug=None):
    # Функция вытаскивает продукты и если слаг приходит заполненным, то фильтр по слагу и в конце возвращаем контексты
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'products': products,
        'categories': categories,
        'category': category
    }
    return render(request, 'product/product_list.html', context=context)


def get_product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'product/product_detail.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # Product.objects.create(**form.cleaned_data)
            return redirect(product.get_absolute_url())

    else:
        form = ProductForm()
    return render(request, 'product/create_product.html', {'product_form': form})


def delete_product(request, product_slug):
    Product.objects.get(slug=product_slug).delete()
    return redirect('/')


def update_product(request, pk):
    post = get_object_or_404(Post, pk=pk)