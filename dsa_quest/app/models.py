from django.db import models


class ProblemModel(models.Model):
    name = ... # str
    slug = ... # slug
    level_of_difficulty = ... # choices
    description: ... # rich text field
