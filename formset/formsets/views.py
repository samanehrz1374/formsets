

# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    # BookFormset,
    # BookModelFormset,
    BookModelForm,
    AuthorFormset
)
from .models import Book, Author
from django.contrib.auth.decorators import login_required

@login_required
def create_book_with_authors(request):
    template_name = 'formsets/create_with_author.html'
    if request.method == 'GET':

        bookform = request.user.profile
        formset = AuthorFormset(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = request.user.profile
        formset = AuthorFormset(request.POST)
        if  formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            # book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.book = bookform 
                author.save()
            return redirect("create_book")
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })