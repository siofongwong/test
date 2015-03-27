from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    git_link = models.CharField(max_length=200)


class Sprint(models.Model):
    project = models.ForeignKey(Project)
    test_case = models.CharField(max_length=200)
