from django.db import models

from books.models import book
from delivery.models import client


# Create your models here.

class buy(models.Model):
    buy_description = models.TextField()
    client_id = models.ForeignKey(client, on_delete=models.CASCADE)

class buy_book(models.Model):
    buy_id = models.ForeignKey(buy, on_delete=models.CASCADE)
    book_id = models.ForeignKey(book, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()

class step(models.Model):
    name_step = models.CharField(max_length=20)

class buy_step(models.Model):
    buy_id = models.ForeignKey(buy, on_delete=models.CASCADE)
    step_id = models.ForeignKey(step, on_delete=models.CASCADE)
    date_step_beg = models.DateField(auto_now=False , auto_now_add=False)