from django.urls import path

from .views import (
    # create_book_normal,
    # create_book_model_form,
    create_book_with_authors,
    # BookListView,
)

app_name = 'store'

urlpatterns = [

    # path(r'^book/create_normal', create_book_normal, name='create_book_normal'),
    # path(r'^book/create_model', create_book_model_form, name='create_book_model_form'),
    path('', create_book_with_authors, name='create_book'),
    # path(r'^book/list', BookListView.as_view(), name='book_list'),

]