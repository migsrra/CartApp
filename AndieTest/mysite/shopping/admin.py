from django.contrib import admin
from .models import Account,Activity,Business,Inventory,Order

# Register your models here.
admin.site.register(Account)
admin.site.register(Activity)
admin.site.register(Business)
admin.site.register(Inventory)
admin.site.register(Order)