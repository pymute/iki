from django.db import models
from datetime import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=20,default='')
    pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.question_text