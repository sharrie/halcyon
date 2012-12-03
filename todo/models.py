from django.db import models
from django.contrib import admin

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=128)
    date_added = models.DateField(auto_now_add=True)
    time_added = models.TimeField(auto_now_add=True)
    date_due = models.DateField(blank=True, null=True)
    time_due = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name","created","done","hidden"]
    search_fields = ["name"]

admin.site.register(Item, ItemAdmin)
