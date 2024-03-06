from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    logo = models.ImageField(blank=True, null=True, upload_to="logo")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



# Still have questions about why use a model to represent media??
class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)


    # This is a custom save method that is executed whenever an instance of the Media model is saved.
    def save(self, *args, **kwargs):
        if self.url:             # if there's a url then set is_mage to false
            self.is_image = False
        # calls the original save method using super to perform the actual saving of the instance.
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    skill = models.ManyToManyField(Skill)
    description = RichTextField(blank=True, null=True)




class Portfolio(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True, null=True)


# class ContactProfile(models.Model):

#     class Meta:
#         verbose_name_plural = 'Contact Profiles'
#         verbose_name = 'Contact Profile'
#         ordering = ["timestamp"]
#     timestamp = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(verbose_name="Name",max_length=100)
#     email = models.EmailField(verbose_name="Email")
#     message = models.TextField(verbose_name="Message")

#     def __str__(self):
#         return f'{self.name}'
