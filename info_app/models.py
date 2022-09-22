from django.db import models


class AboutUs(models.Model):
    description = models.TextField(
        verbose_name='О компании',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class Contact(models.Model):
    phone_number = models.IntegerField()
    insta = models.URLField()
    facebook = models.URLField()
    email = models.EmailField()
    location = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class OurMission(models.Model):
    our_mission = models.TextField()

    class Meta:
        verbose_name = 'Наша миссия'
        verbose_name_plural = 'Наша миссия'


class Logo(models.Model):
    logo = models.ImageField()

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотип'



