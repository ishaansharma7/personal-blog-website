from django.contrib import admin
from .models import PostDetail
# Register your models here.
@admin.register(PostDetail)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('post_title',),}