from django.db.models.fields.files import ImageField
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class AdminPhotoWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        t = ""
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        if value and getattr(value, "url", None):
            image_url = value.url
            t = render_to_string("crop.html", {"crop_url": image_url})
            output.append(t)
        return mark_safe(''.join(output))
