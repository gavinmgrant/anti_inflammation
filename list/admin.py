from django.contrib import admin
from . models import Food, Source, Category, List

# Register your models here.
admin.site.register(Food),
admin.site.register(Source),
admin.site.register(Category),
admin.site.register(List),