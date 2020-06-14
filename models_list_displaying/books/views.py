from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def books_date(request, date):
    template = 'books/books_list.html'
    dates = []
    for i in Book.objects.all():
        dates.append(i.pub_date)
    dates = sorted(set(dates))
    print(dates)
    if date:
        books = Book.objects.filter(pub_date=date)
    # page = int(request.GET.get('page', 1))
    # paginator = Paginator([1,2,3], 10)
    # page_object = paginator.get_page(page)

    current_page = date
    current_page_index = dates.index(date)
    print(current_page_index)
    print(len(dates))
    if current_page_index + 1 >= len(dates):
        print('1')
        next_page = None
    elif current_page_index+1 < len(dates):
        next_page = dates[current_page_index+1]
    if current_page_index - 1 < 0:
        prev_page = None
    else:
        prev_page = dates[current_page_index - 1]
    context = {'books': books,
               'prev_page': prev_page,
               'next_page': next_page,
               'current_page': current_page}
    return render(request, template, context)