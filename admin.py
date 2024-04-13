
from django.contrib import admin
from .models import Gallery, Photo
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.db.models.fields.files import ImageField
from .widget import AdminPhotoWidget

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "available", "code",)
    list_filter = ("name", "available", "code",)
    search_fields = ("name", "available", "code",)
    ordering = ('id',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = ('id',)
    formfield_overrides = {
        ImageField: {'widget': AdminPhotoWidget},
    }
