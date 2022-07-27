from django.db import models
from common.models import User

from helpers.models import BaseModel

vacancy_type_choices = (
    ("oddiy", "oddiy"),
    ("premium", "premium"),
    ("shoshilinch", "shoshilinch")
)


# Create your models here.
class Vacancy(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post")
    description = models.TextField()
    vacancy_type = models.CharField(max_length=200,choices=vacancy_type_choices)
