from django.contrib import admin
from school_store_app.models import Departments, Courses, Detail, Purpose, Materials


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Departments, DepartmentsAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']


admin.site.register(Courses, CoursesAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Detail, DetailsAdmin)


class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Purpose, PurposeAdmin)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Materials, MaterialsAdmin)

