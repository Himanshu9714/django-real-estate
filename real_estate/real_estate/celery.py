from __future__ import absolute_import
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_estate.settings.development")

app = Celery("real_estate")
app.config_from_object("real_estate.settings.development", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
