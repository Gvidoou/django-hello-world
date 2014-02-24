from django.db import models


class Person(models.Model):
    """
    Creates person model with cells for adding personal data
    """
    name = models.CharField(max_length= 20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    biography = models.TextField(max_length=500)
    birth_date = models.DateField(auto_now_add=False)
    email = models.EmailField(max_length=75, blank=False)
    skype = models.CharField(max_length=50)
    jabber = models.CharField(max_length=50)
    other_contacts = models.TextField(max_length=50)

    def __unicode__(self):
        return self.name