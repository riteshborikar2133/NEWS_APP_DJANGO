from django.contrib import admin
from .models import Category 
from .models import News
from .models import Comment
# Register your models here.

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title','Category','add_time')
admin.site.register(News,AdminNews)

class AdminCommnet(admin.ModelAdmin):
    list_display=('news','email','comment','status')
admin.site.register(Comment,AdminCommnet)