from django.db import models


class TextPresentation(models.Model):
    text = models.TextField()


class Opinion(models.Model):
    author = models.TextField(max_length=40)
    post = models.TextField(max_length=300)
    is_valid = models.BooleanField(default=False)


class OsteopathyAbout(models.Model):
    text_where = models.TextField()
    text_who = models.TextField()
    text_advantages = models.TextField()


class OsteopathyCase(models.Model):
    title = models.TextField(max_length=40)
    description = models.TextField()
    image = models.ImageField()


class OsteopathyHistory(models.Model):
    text = models.TextField()


class Appointment(models.Model):
    duration_min = models.IntegerField(default=60)
    date = models.DateField()
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    description = models.TextField()


class AppointmentsDescription(models.Model):
    text = models.TextField()
