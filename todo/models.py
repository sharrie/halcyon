from django.db import models
from django.contrib import admin

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name","created","done","hidden"]
    search_fields = ["name"]

admin.site.register(Item, ItemAdmin)
