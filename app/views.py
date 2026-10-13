from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()           
    return render(request, "index.html", {"books": books})


def create(request):
    if request.method == "POST":
        Book.objects.create(
            name=request.POST.get('name'),
            author=request.POST.get('author'),
            price=request.POST.get('price') or 0
        )
        return redirect('index')
    return render(request, "form.html")


def update(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "POST":
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.save()
        return redirect('index')
    return render(request, "form.html", {"book": book})


def delete(request, pk):
    get_object_or_404(Book, id=pk).delete()
    return redirect('index')



