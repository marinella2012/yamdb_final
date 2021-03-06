from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title import Title


class Review(models.Model):
    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(get_user_model(),
                               verbose_name='Ревьюер',
                               on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            )
        ]

    def __str__(self):
        return self.text[:15]
