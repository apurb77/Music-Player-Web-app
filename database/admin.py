from django.contrib import admin

from database.models import Contact, Addressbook,Playlist,Arijit_Song

# Register your models here.

admin.site.register(Contact)
admin.site.register(Addressbook)
admin.site.register(Playlist)
admin.site.register(Arijit_Song)

