from django.db import models

class Blog_Post(models.Model):
    Title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)

    def SummaryOfBlog(self):
        return self.content[:200]


    def __str__(self):
        return self.Title  
