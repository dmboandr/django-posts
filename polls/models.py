from django.db import models

# Create your models here.
"""
ЭТО ФАЙЛ models.py
Здесь мы будем создавать модели базы данных
(т.е. какие переменные и как они связаны)
"""

class Question(models.Model):  # здесь класс наследуется от инструмента Django
    question_text = models.CharField(max_length=200)  # будет текст на 200 символов
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # это вторичный ключ, связывающий варианты ответа с конкретный вопросом
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # здесь описание ответа на вопрос
    votes = models.IntegerField(default=0)  # количество проголосовавших за этот выбор в этом опросе

    def __str__(self):
        return self.choice_text

"""
1, 3, Решка, 10
2, 3, Орёл, 15
"""
