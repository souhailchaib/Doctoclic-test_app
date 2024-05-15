from django.core.management.base import BaseCommand
from test_app.faker import Faker
from app.models import MedecinModel  # Import your ClientModel here


class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(100):  # Generate 2000 fake records
            # Create a new instance of ClientModel with fake data
            medecin = MedecinModel(
                nom=fake.last_name(),
                prenom=fake.first_name(),
            )
            medecin.save()
        self.stdout.write(self.style.SUCCESS("Fake data populated successfully"))
