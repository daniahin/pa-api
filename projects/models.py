from django.db import models

class Project(models.Model):
    projectName = models.CharField(max_length=30, unique=True)
    projDescription = models.TextField(max_length=100, blank=True, null=True)
    authorName = models.CharField(max_length=30, blank=True, null=True)
    projBrief = models.ImageField(upload_to="briefs/", blank=True, null=True)
    isPublic = models.BooleanField(default=True)

    def __str__(self):
        return self.projectName
