from django.contrib import admin
from .models import teacher, group, subject, classroom, Class

admin.site.register(teacher)
admin.site.register(group)
admin.site.register(subject)
admin.site.register(classroom)
admin.site.register(Class)
