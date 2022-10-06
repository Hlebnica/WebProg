from django.shortcuts import render
from .models import Books
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    # Получение всех записей
    books = Books.objects.all()

    # Пагинация
    paginator = Paginator(books, 3)
    page = request.GET.get("page")

    try:
        page_books = paginator.get_page(page)
    except PageNotAnInteger:
        page_books = paginator.get_page(1)
    except EmptyPage:
        page_books = paginator.get_page(paginator.num_pages)

    for book in page_books:
        print(book.title)

    data = {"page": page, "page_books": page_books}

    # Вывод в index.html
    return render(request, "index.html", context=data)


def create(request):  # Создание

    if request.method == "GET":
        return render(request, "create.html")
    book = Books()
    book.title = request.POST.get("title")
    book.author = request.POST.get("author")
    book.price = request.POST.get("price")
    book.save()
    return HttpResponseRedirect("/")


def edit(request, id):  # Обновление по id
    try:
        book = Books.objects.get(id=id)

        if request.method == "POST":
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.price = request.POST.get("price")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"book": book})
    except Books.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


def delete(request, id):  # Удаление по id
    try:
        book = Books.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except Books.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")
