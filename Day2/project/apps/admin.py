from django.contrib import admin
from .models import Project , Review , Tag# databse class name 

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)

# Register your models here.
