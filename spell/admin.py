from django.contrib import admin

from .models import Question, SpellBook, PersonList

admin.site.register(Question)
admin.site.register(SpellBook)
admin.site.register(PersonList)
# Register your models here.
