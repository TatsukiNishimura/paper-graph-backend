from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    abstract = models.TextField()
    doi = models.CharField(max_length=100, unique=True)
    citations = models.ManyToManyField(
        "self", symmetrical=False, related_name="cited_by", blank=True
    )
    paper_url = models.URLField(default="")

    def __str__(self):
        return self.title
