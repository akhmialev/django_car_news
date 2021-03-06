from django.db import models
from django.urls import reverse


class Car(models.Model):                                            # Населдуемся именно от сюда
    title = models.CharField(max_length=255, verbose_name="Марка")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name="Текст статьи")                          # blank=True пустое поле
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')         # ссылка на наше фото
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')           # создание статьи(текущее значение времени при создании)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')               # изменение статьи(время меняеться всегда при изменении)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT, verbose_name='Категория')    # FofeigKey связывает таблицу Car с Таблицей Category в бд(связь все к одному),on_delete=models.PROTECT - запрешает удалять категории
                                                                        # Category в ковычках потому что класс Category создан после класса Car, если перенести до тогда можно без ковычек
    def __str__(self):                                              # null=True ставиться для того что бы заполнить колонку нулями, т.к. мы создаем таблицу категории после кар, лучше сразу создавать все нужные таблицы!
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Марку автомобиля"
        verbose_name_plural = "Марки автомобилей"
        ordering = ['time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Страна производителя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Производителя"
        verbose_name_plural = "Страны производители"
        ordering = ['id']
