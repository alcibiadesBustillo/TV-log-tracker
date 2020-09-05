from django.contrib import admin
from .models import Category, Show, Spent

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



class SpentInline(admin.StackedInline):
    model = Spent
    

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    inlines = [SpentInline,]
