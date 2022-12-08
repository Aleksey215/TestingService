from django.db import models


class Theme(models.Model):
    """
    Themes for test sets
    """
    theme_name = models.CharField(max_length=64)

    def __str__(self):
        return self.theme_name


class Set(models.Model):
    """
    Test sets
    """
    set_name = models.CharField(max_length=64)
    set_theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    set_result = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Test sets"

    def __str__(self):
        return self.set_name


class Test(models.Model):
    """
    Item of test set
    """
    test_name = models.CharField(max_length=64)
    test_result = models.PositiveIntegerField(default=0)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Question(models.Model):
    """
    Item of test
    """
    question_name = models.CharField(max_length=64)
    question_content = models.TextField()
    answered = models.BooleanField(default=False)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    ans = models.ManyToManyField('Answer', v)

    def __str__(self):
        return self.question_name


class Answer(models.Model):
    """
    Item of question
    """
    answer_content = models.TextField()
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.question_name}/{self.correct}'
