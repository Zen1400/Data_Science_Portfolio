from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile
# UserProfile.objects.create(): This is using the create() method provided by Django's ORM
# (Object-Relational Mapping) to create a new instance of the UserProfile model and save it to the database in a single step.

# The post_save signal is emitted after a model's save() method is successfully called.
#  post_save signal is to perform additional actions or tasks after saving an instance of a model
@receiver(post_save, sender=User)
# Called when the reciever gets post_save signal from the User
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = UserProfile.objects.create(user=instance)
