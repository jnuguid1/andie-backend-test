from django.contrib import admin

from .models import Account, Activity, Business, Item

admin.site.register(Account)
admin.site.register(Activity)
admin.site.register(Business)
admin.site.register(Item)