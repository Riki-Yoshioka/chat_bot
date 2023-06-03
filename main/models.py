from django.db import models

class Dialogue(models.Model):
    message = models.CharField(max_length=500)
    send_bot = models.BooleanField()
    send_date = models.DateTimeField("date published")

class Q_A(models.Model):
    user_input = models.CharField(max_length=500)
    bot_reply = models.CharField(max_length=500)
