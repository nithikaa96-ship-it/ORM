from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid', 'name', 'salary', 'age', 'email')

admin.site.register(Employee, EmployeeAdmin)