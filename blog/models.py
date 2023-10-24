from django.db import models

# Create your models here.
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Blog(models.Model):
    """
    Model representing a blog post.

    Fields:
    - title (CharField): The title of the blog post.
    - body (TextField): The content of the blog post.
    - preview (ImageField): An optional preview image for the blog post.
    - create_date (DateTimeField): The date and time when the blog post was created (auto-generated).
    - tag (CharField with choices): The tag/category of the blog post.
    - views_count (PositiveSmallIntegerField): The number of views for the blog post (auto-incremented).
    """
    TAG_CHOICES = [
        ('news', 'Новости'),
        ('event', 'События'),
        ('useful material', 'Полезные материалы'),
        ('research', 'Исследования'),
        ('new test', 'Новые тесты'),
    ]
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    tag = models.CharField(max_length=15, choices=TAG_CHOICES, default=TAG_CHOICES[0][0], verbose_name='Тег')
    views_count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество просмотров', editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ['-create_date']
