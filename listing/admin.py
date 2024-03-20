from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Listing
class ListingAdmin(admin.ModelAdmin):
    using = 'listings'
    list_display = ('id', 'realtor', 'title', 'slug', )
    list_display_links = ('id', 'realtor', 'title', 'slug', )
    list_filter = ('realtor', )
    search_fields = ('title', 'description', )
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).using(self.using)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs: Any):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs: Any):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
    

admin.site.register(Listing, ListingAdmin)