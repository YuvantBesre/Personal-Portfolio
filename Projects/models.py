from django.db import models

class Project(models.Model):
    Image = models.ImageField(upload_to='images/')
    Summary = models.CharField(max_length=1000)
    GitHub = models.URLField(blank=True)

    def __str__(self):
        return self.Summary




