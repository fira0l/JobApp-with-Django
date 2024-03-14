from django.contrib import admin

from subscribe.models import Subscribe

# Register your models here.

class subscribeAdmin(admin.ModelAdmin):
    list_display= ('__str__','first_name','last_name')
    search_fields = ('first_name','last_name','email')
    search_help_text = "INSERT YOUR QUERY AND PRESS ENTER"
    list_filter = ('email',)


admin.site.register(Subscribe,subscribeAdmin)