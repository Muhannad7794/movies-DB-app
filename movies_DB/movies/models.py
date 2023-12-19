from django.db import models

class MovieInfo(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    director = models.ForeignKey("Directors", on_delete=models.CASCADE)
    credits_score = models.FloatField()
    studio = models.ForeignKey("Studios", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Directors(models.Model):
    director_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    director_date_of_birth = models.DateField()
    director_best_movies = models.CharField(max_length=215)
    awards = models.CharField(max_length=100)

    def __str__(self):
        return self.director_name

class Studios(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
