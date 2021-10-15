from django.shortcuts import render

from mainapp.models import Product
from mainapp.models import Contact


def main(request):
    title = "Магазин"

    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = "Контакты"

    contacts = Contact.objects.all()[:3]

    context = {
        'title': title,
        'contacts': contacts,
    }
    return render(request, 'geekshop/contact.html', context)
