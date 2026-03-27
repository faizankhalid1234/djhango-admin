from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "age", "branch")
    search_fields = ("username", "email")
    list_filter = ("branch",)
