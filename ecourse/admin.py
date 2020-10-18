from django.contrib import admin

# Register your models here.
from .models import Accounts,Courses,Videos,Comments

admin.site.register(Accounts)
admin.site.register(Courses)
admin.site.register(Videos)
admin.site.register(Comments)