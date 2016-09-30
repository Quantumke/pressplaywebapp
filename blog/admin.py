from django.contrib import admin
from blog.models import Category,Entry, Link, Trending, fakeusers

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={ 'slug':['title'] }

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':['title']}


admin.site.register(Entry, EntryAdmin)

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}

admin.site.register(Link, LinkAdmin)

class TrendingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}

admin.site.register(Trending, TrendingAdmin)

class fakeusersAdmin(admin.ModelAdmin):
    pass
admin.site.register(fakeusers, fakeusersAdmin)
