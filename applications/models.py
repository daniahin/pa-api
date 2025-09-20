from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

CONTACT_CHOICES = [
    ('phone', 'Phone'),
    ('email', 'Email'),
    ('telegram', 'Telegram'),
]

TECH_CHOICES = [
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('fullstack', 'Fullstack'),
]

class Application(models.Model):
    firstName = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
            RegexValidator(r'^[A-Za-z\-]+$', 'Тільки літери та дефіс')
        ]
    )
    lastName = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
            RegexValidator(r'^[A-Za-z\-]+$', 'Тільки літери та дефіс')
        ]
    )
    contactMethod = models.CharField(max_length=8, choices=CONTACT_CHOICES)
    phone = models.CharField(
        max_length=11,
        blank=True, null=True,
        validators=[RegexValidator(r'^\d{11}$', 'Повинно бути 11 цифр')]
    )
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(
        max_length=32,
        blank=True, null=True,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(32),
            RegexValidator(r'^[A-Za-z0-9_]+$', 'Тільки літери, цифри та нижнє підкреслення')
        ]
    )
    technologies = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
