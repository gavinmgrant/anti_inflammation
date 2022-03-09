from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, unique=True)
  category = models.ManyToManyField('Category', related_name='foods')
  source = models.ManyToManyField('Source', related_name='foods')
  in_moderation = models.BooleanField(default=False)

  def __str__(self):
    return self.name

class Source(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, unique=True)
  url = models.CharField(max_length=200, default="")

  def __str__(self):
    return self.name

class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.name

class List(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField('Food', related_name='lists')

    def __str__(self):
      return f"{self.user}'s list"
