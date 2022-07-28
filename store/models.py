from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Flowers(models.Model):
    title = models.TextField("Название", max_length=250, blank=True)
    price = models.CharField("Цена", max_length=50, blank=True)
    img = models.ImageField("Изоброжения", upload_to="flowers/")
    description = models.TextField("Описание", max_length=500, blank=True)
    url = models.SlugField(max_length=130, unique=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)
   
    def get_absolute_url(self):
        return reverse("flowers_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Растения'
        verbose_name_plural = 'Растения'

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE, verbose_name="цветок", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.flowers}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    flowers = models.ForeignKey(Flowers, verbose_name="цветок", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.flowers}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"