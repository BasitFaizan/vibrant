from django.contrib import admin
from Projects.models import Projectcard
from authentication.models import customUser


admin.site.register(customUser)
admin.site.register(Projectcard)
