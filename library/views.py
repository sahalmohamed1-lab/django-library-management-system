from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "library/home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "library/register.html", {"form": form})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "library/book_form.html", {"form": form})