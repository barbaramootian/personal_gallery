from django.contrib import admin
from .models import Image,Location,Category

# Register your models here.
# Adding Models to the Admin
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)