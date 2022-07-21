from django.contrib import admin

from .models import Origami, Decorated, Material

# Register your models here.
admin.site.register(Origami)
admin.site.register(Decorated)
admin.site.register(Material)
