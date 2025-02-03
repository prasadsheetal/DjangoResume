from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=200)
    bio = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    projects = models.TextField()
    extracurricular = models.TextField()
