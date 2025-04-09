from django.contrib import admin
from courses.models import Course , Preriquisite ,Learning , Tag , Video


# Register your models here.

# class TagAdmin(admin.TabularInline):
#     model = Tag

# class LearnigAdmin(admin.TabularInline):
#     model = Learning

# class PreriquisiteAdmin(admin.TabularInline):
#     model = Preriquisite  

# class CourseAdmin(admin.ModelAdmin):
#     inline = [TagAdmin ]

admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Learning)
admin.site.register(Preriquisite)
admin.site.register(Video)