from django.db import models

class Article(models.Model):
    title  = models.CharField(max_length=30)
    contents = models.TextField()
    viewcount = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title, self.viewcount)


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
