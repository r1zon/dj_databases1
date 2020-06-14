from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        files = list(Phone.objects.order_by('name'))
    elif sort == 'min_price':
        files = list(Phone.objects.order_by('price'))
    elif sort == 'max_price':
        files = list(Phone.objects.order_by('-price'))
    else:
        files = list(Phone.objects.all())
    context = {'files': files}
    print(files[0].release_date)
    return render(request, template, context, sort)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.filter(slug = slug)
    context = {'product': product[0]}
    return render(request, template, context)
