from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Book(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,related_name="profile",null=True)
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

    def get_authors(self):
        return ', '.join(self.authors.all().values_list('name', flat=True))


class Author(models.Model):

    name = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name