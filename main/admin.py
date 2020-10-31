

# Register your models here.
from django.contrib import admin
from .views import About,Service,RecentWork

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)

