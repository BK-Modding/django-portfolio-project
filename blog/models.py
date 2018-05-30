from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.description[:100] + "......."

    def pubdatepretty(self):
        return self.pubdate.strftime('%b %e, %Y')

    def __str__(self):
        return self.title