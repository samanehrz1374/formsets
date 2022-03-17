from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Book(models.Model):
    # user=models.OneToOneField(User,on_delete=CASCADE,related_name="profile",null=True)
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    # class Meta:
    #     db_table = 'book'

    def __str__(self):
        return self.name

    # def get_authors(self):
    #     return ', '.join(self.authors.all().values_list('name', flat=True))


class Author(models.Model):

    name = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name


class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,verbose_name="کاربری",related_name="profile")
    # name = models.CharField(max_length=20,null=True) 

    # def __str__(self):
    #     return self.user

class skillsModel(models.Model):
    skillname=models.CharField(max_length=100,verbose_name="مهارت")
    Basic=1
    intermidiate=2
    advanced=3
    status_choices=((Basic,"مقدماتی"),
                    (intermidiate,"متوسط"),
                    (advanced,"پیشرفته"))
    levelofskill=models.IntegerField(choices=status_choices,verbose_name="سطح مهارت")
    skills = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.skillname