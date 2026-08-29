# management/commands/translate_laws.py
from django.core.management.base import BaseCommand
from law.models import *
from right.models import *
from deep_translator import GoogleTranslator  # More reliable alternative

class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in [ConsumerProtection]:  # Add all models
            self.stdout.write(f"Translating {model.__name__}...")
            for law in model.objects.filter(title_ta__isnull=True)[:107]:  # Translate up to 107 records
                try:
                    law.summary_ta = GoogleTranslator(source='en', target='ta').translate(law.summary)
                    law.title_ta = GoogleTranslator(source='en', target='ta').translate(law.title)
                    law.name_ta = GoogleTranslator(source='en', target='ta').translate(law.name)
                    law.save()
                except Exception as e:
                    self.stdout.write(f"Error in {law.section}: {str(e)}")