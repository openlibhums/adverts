import uuid
import os

from django.db import models
from django.utils import timezone

from core.file_system import JanewayFileSystemStorage

fs = JanewayFileSystemStorage()


def advert_images_upload_path(instance, filename):
    try:
        filename = str(uuid.uuid4()) + '.' + str(filename.split('.')[1])
    except IndexError:
        filename = str(uuid.uuid4())

    path = "profile_images/"
    return os.path.join(path, filename)


def advert_display_choices():
    return (
        ('carousel', 'Carousel'),
        ('issue_left', 'Issue Left'),
        ('issue_right', 'Issue Right'),
    )


class Advert(models.Model):
    journal = models.ForeignKey(
        'journal.Journal',
        on_delete=models.CASCADE,
    )
    issue = models.ForeignKey(
        'journal.Issue',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=255,
        help_text='Text to identify this advert.',
    )
    image = models.ImageField(
        upload_to=advert_images_upload_path,
        storage=fs,
    )
    start_display = models.DateTimeField(
        default=timezone.now,
    )
    end_display = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Leave blank to always display this advert.',
    )
