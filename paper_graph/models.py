from django.db import models


class Paper(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    abstract = models.TextField(blank=True)
    doi = models.CharField(max_length=100, blank=True)
    citations = models.ManyToManyField(
        "self", symmetrical=False, related_name="cited_by", blank=True
    )
    paper_url = models.URLField(default="", blank=True)

    def __str__(self):
        return self.title
