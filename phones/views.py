from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_for_context = []

    sort_by = request.GET.get('sort')

    if sort_by is None:
        phone_objects = Phone.objects.all()
    elif sort_by == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort_by == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort_by == 'max_price':
        phone_objects = Phone.objects.order_by('-price')

    for phone in phone_objects:
        phone_for_context = {'name': phone.name,
                             'price': phone.price,
                             'image': phone.image,
                             'slug': phone.slug}
        phones_for_context.append(phone_for_context)
    return render(request, template, context={'phones': phones_for_context})


def show_product(request, slug):
    template = 'product.html'
    phone_for_context = {}
    phone_object = Phone.objects.filter(slug=slug)
    phone_for_context['name'] = phone_object[0].name
    phone_for_context['image'] = phone_object[0].image
    phone_for_context['price'] = phone_object[0].price
    phone_for_context['release_date'] = phone_object[0].release_date
    phone_for_context['lte_exists'] = phone_object[0].lte_exists

    return render(request, template, context={'phone': phone_for_context})
