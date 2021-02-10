from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self) -> None:
        return self.name


class BannedCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> None:
        return self.name
