from django.contrib import admin
from .models import Bookmark
# Register your models here.

admin.site.register(Bookmark)
# -> db에 적용을 한다