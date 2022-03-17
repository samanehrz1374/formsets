

# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    # BookFormset,
    # BookModelFormset,
    BookModelForm,
    AuthorFormset,
    LanguageFormset
)
from .models import Book, Author, ProfileModel,skillsModel
from django.contrib.auth.decorators import login_required
from django.forms import (formset_factory, modelformset_factory,inlineformset_factory)



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



def index(request, programmer_id):
    programmer = ProfileModel.objects.get(pk=programmer_id)
    Languageformset = LanguageFormset(skillsModel.objects.all())

    if request.method == 'POST':
        if 'skilledit' in request.POST:
            formset = LanguageFormset(request.POST, instance=programmer)
            if formset.is_valid():
                formset.save()
                return redirect('index', programmer_id=programmer.id)

    formset = LanguageFormset(instance=programmer)

    return render(request, 'formsets/index.html', {'formset' : formset})