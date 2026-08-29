from django.db import models

class Amendment(models.Model):
    law_table = models.CharField(max_length=100)
    section_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('New', 'New'), ('Updated', 'Updated'), ('Repealed', 'Repealed'), ('Amended', 'Amended')
    ])
    description = models.TextField()
    date_enacted = models.DateField()

    def __str__(self):
        return f"{self.status} - {self.law_table} (Sec {self.section_id})"

class RelatedLaw(models.Model):
    primary_law_table = models.CharField(max_length=100)
    primary_section_id = models.CharField(max_length=100)
    related_law_table = models.CharField(max_length=100)
    related_section_id = models.CharField(max_length=100)
    relationship_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.primary_law_table} -> {self.related_law_table}"

