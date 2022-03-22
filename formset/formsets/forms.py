from django import forms
from django.forms import (formset_factory, modelformset_factory,inlineformset_factory)

from .models import (Book, Author,ProfileModel,skillsModel)


# class BookForm(forms.Form):
#     name = forms.CharField(
#         label='Book Name',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Book Name here'
#         })
#     )


class BookModelForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ()
        # labels = {
        #     'name': 'Book Name'
        # }
        # widgets = {
        #     'name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Book Name here'
        #         }
        #     )
        # }


# BookFormset = formset_factory(BookForm)
# BookModelFormset = modelformset_factory(
#     Book,
#     fields=('name', ),
#     extra=1,
#     widgets={
#         'name': forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Book Name here'
#             }
#         )
#     }
# )

AuthorFormset = modelformset_factory(
    Author,
    fields=('name', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Author Name here'
        })
    }
)

LanguageFormset = inlineformset_factory(ProfileModel, skillsModel,
 fields=('skillname','levelofskill'),
 extra=0,
 error_messages={
    'skillname': {
        'required': 'some custom required message',
    },
    'levelofskill': {
        'required': 'some required message',
    },
 }
 
 )