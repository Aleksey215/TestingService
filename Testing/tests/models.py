from django.db import models


class Theme(models.Model):
    theme_name = models.CharField(max_length=64)

    def __str__(self):
        return self.theme_name


class Set(models.Model):
    set_name = models.CharField(max_length=64)
    set_theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    set_result = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.set_name


class Test(models.Model):
    test_name = models.CharField(max_length=64)
    test_result = models.PositiveIntegerField(default=0)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Question(models.Model):
    question_name = models.CharField(max_length=64)
    question_content = models.TextField()
    answered = models.BooleanField(default=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name


class Answer(models.Model):
    answer_content = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.question_name}/{self.correct}'
