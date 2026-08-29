from django.core.management.base import BaseCommand
from law.models import *

class Command(BaseCommand):
    help = "Reset Tamil translation fields to NULL in all law models"

    def handle(self, *args, **kwargs):
        models = [
            Bns
        ]

        for model in models:
            updated = model.objects.update(
                title_ta=None,
                name_ta=None,
                summary_ta=None
            )
            self.stdout.write(f"{model.__name__}: {updated} rows reset.")
