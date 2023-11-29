from django.db import models

# Music model.
class Music(models.Model):
    title = models.CharField(max_length=100)
    lyrics = models.TextField()
    file = models.FileField(upload_to='music/')
    total_ratings = models.PositiveIntegerField(default=0)
    total_rating_value = models.PositiveIntegerField(default=0)

    def average_rating(self):
        if self.total_ratings == 0:
            return 0
        return self.total_rating_value / self.total_ratings

    def __str__(self):
        return self.title