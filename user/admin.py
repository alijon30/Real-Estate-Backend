from django.contrib import admin
from django.contrib.auth import get_user_model
from typing import Any
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query import QuerySet
from django.http import HttpRequest
from listing.extras import delete_realtors_listing_data
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    using = 'users'
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name', 'email', )
    search_fields = ('name', 'email', )
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        email = obj.email
        obj.delete(using=self.using)
        delete_realtors_listing_data(email)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).using(self.using)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs: Any):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs: Any):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
    

admin.site.register(User, UserAdmin)