from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display    = ('text', 'owner', 'created_at')

admin.site.register(Note, NoteAdmin)
