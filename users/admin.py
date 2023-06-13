from django.contrib import admin

# Register your models here.
from .models import User
# Register your models here.
from .models import Profile

admin.site.register(Profile)

admin.site.register(User)