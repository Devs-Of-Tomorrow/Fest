from django.db import models
from django.db.models.functions import Coalesce

class CustManager(models.Manager):
    def with_counts(self):
        return self.annotate(
            num_responses=Coalesce(models.Count("response"), 0)
        )
