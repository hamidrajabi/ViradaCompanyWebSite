from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Header)
admin.site.register(Slider)
admin.site.register(OurWork)
admin.site.register(Tag)
class WorkItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
admin.site.register(WorkItem,WorkItemAdmin)
# admin.site.register(WorkItem)
admin.site.register(ClientCompany)
admin.site.register(OurService)