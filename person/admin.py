from django.contrib import admin

# Register your models here.
from .models import Person,Article

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age',)   #list_display 就是来配置要显示的字段的


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_date','update_time',)

admin.site.register(Person,PersonAdmin)

admin.site.register(Article,ArticleAdmin)