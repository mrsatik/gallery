from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'
    verbose_name = _("Gallery and crop images")
