from django.contrib import admin

from .models import Account, Activity, Business, Item, Order

admin.site.register(Account)
admin.site.register(Activity)
admin.site.register(Business)
admin.site.register(Item)
admin.site.register(Order)