from django.db import models


class Url(models.Model):
    id = models.IntegerField(name="id", primary_key=True)
    link = models.CharField(name="link", max_length=50)
    created_at = models.DateTimeField(name="created_at", auto_now=True)
    visits = models.IntegerField(name="visits", default=1)

    def __str__(self) -> str:
        return f'Url(id={self.id}, link={self.link}, created_at={self.created_at}, visits={self.visits})'

    def __repr__(self):
        return self.__str__()
