from django.db import models

class Links(models.Model):
    urls = models.CharField(max_length = 200)
    slug = models.CharField(max_length= 15)
    def __str__ (self):
        return self.urls
