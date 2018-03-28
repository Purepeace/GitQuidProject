from django.contrib import admin
from GitQuid.models import *
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Donation)
admin.site.register(Project, MarkdownxModelAdmin)
