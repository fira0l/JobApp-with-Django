from django.contrib import admin
from app.models import JobPost,Location,Author,Skills


# Register your models here.
class JobAdmin(admin.ModelAdmin):
   list_display = ('__str__','title','salary','date')
   list_filter= ('date','salary','expiry') 
   search_fields= ('title','description')
   search_help_text= 'Type in Your QUERY and Hit ENTER'
#    fields= (('title','description'),'expiry')
   fieldsets =(
       ('Basic information',
                {'fields':('title','description','location','author','skills')}
                ),
       ('More Information',
                {
                   'classes':('collapse','wide'),
                   'fields':(('salary','expiry'),'slug')}
                ),
               )
class LocationAdmin(admin.ModelAdmin):
   list_display =('__str__','street','city','country')
   list_filter = ('street','country','zip')
   search_fields= ('street','country','zip')
   search_help_text = "Type in your QUERY and Hit ENTER"
   
class AuthorAdmin(admin.ModelAdmin):
   list_display=('__str__','name','compony')
   
class SkillsAdmin(admin.ModelAdmin):
   list_display=('__str__','name')

admin.site.register(JobPost,JobAdmin)
admin.site.register(Location,LocationAdmin) 
admin.site.register(Author,AuthorAdmin)
admin.site.register(Skills,SkillsAdmin)