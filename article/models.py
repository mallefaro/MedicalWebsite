from django.db import models

MAX_TEXT_LENGTH = 200
class Article(models.Model):
    article_title = models.CharField(max_length= 200)
    article_text = models.TextField()
    article_date = models.DateField()

    class Meta:
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_short_text(self):
        if len(self.article_text) > MAX_TEXT_LENGTH:
            return self.article_text[:MAX_TEXT_LENGTH]
        else:
            return self.article_text
