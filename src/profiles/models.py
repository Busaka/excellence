from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    # bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    status = models.CharField("Status", max_length=200, blank=True, null=True)
    school = models.CharField("School Name", max_length=200, blank=True, null=True)
    school_phone = models.CharField("School Phone", max_length=200, blank=True, null=True)
    school_email = models.EmailField("School Email", max_length=200, blank=True, null=True)
    website = models.CharField("School Website", max_length=200, blank=True, null=True)
    location = models.CharField("Location", max_length=200, blank=True, null=True)
    user_phone = models.CharField("Your Phone Number", max_length=200, blank=True, null=True)
    study_level = models.CharField("Study Level(Student Only)", max_length=200, blank=True, null=True)
    career1 = models.CharField("First Career  Option(Student Only)", max_length=200, blank=True, null=True)
    career2 = models.CharField("Second Career Option(Student Only)", max_length=200, blank=True, null=True)
    career3 = models.CharField("Third Career Option(Student Only)", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
