from django.contrib import admin
from .models import Category, Show, Spent

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Show)
class ShoewAdmin(admin.ModelAdmin):
    pass

@admin.register(Spent)
class SpentAdmin(admin.ModelAdmin):
    pass