from django.contrib import admin

from .models import Services
from .models import Project
from .models import ContactInfo
from .models import SubscribedUser
# Register your models here.
admin.site.register(Services)
admin.site.register(Project)
admin.site.register(ContactInfo)
admin.site.register(SubscribedUser)