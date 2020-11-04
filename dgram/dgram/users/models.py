from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(AbstractUser, TimeStamedModel):
    """Default user for dstagram."""
    GENDER_CHOICE =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255)
    gender  = models.CharField(blank=True, choices=GENDER_CHOICE, max_length=255)
    followers = models.ManyToManyField("self")
    followeing = models.ManyToManyField("self")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
