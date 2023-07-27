from django.db import models

# Create your models here.

class author(models.Model):
    name_author = models.CharField(max_length=20)

    def __str__(self):
        return self.name_author

class genre(models.Model):
    name_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.name_genre

class book(models.Model):
    title = models.CharField(max_length=100)
    author_id = models.ForeignKey(author, on_delete=models.PROTECT)
    genre_id = models.ForeignKey(genre, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.title