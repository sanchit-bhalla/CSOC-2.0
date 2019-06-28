from django.contrib import admin
from .models import *
from django.db import models
from django.forms import ClearableFileInput


admin.site.register(Departments)
admin.site.register(Subject)
admin.site.register(PdfFiles)
admin.site.register(Notes)
