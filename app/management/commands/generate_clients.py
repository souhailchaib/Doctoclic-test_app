from django.core.management.base import BaseCommand
from faker import Faker
from app.models import ClientModel  # Import your ClientModel here


class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(2000):  # Generate 2000 fake records
            # Create a new instance of ClientModel with fake data
            client = ClientModel(
                client_num_dossier=fake.random_int(min=10000, max=99999),
                client_num=fake.random_number(digits=5),
                client_nom=fake.last_name(),
                client_prenom=fake.first_name(),
                client_nom_prenom=fake.name(),
                client_prenom_nom=fake.name(),
                client_mail=fake.email(),
                client_telephone=fake.phone_number(),
                client_type=fake.random_element(elements=("A", "B", "C")),
                client_datenaissance=fake.date_of_birth(minimum_age=18, maximum_age=90),
                client_uuid=fake.uuid4(),
                client_code_postale=fake.postcode(),
                client_language=fake.language_name(),
                client_commentaire=fake.text(max_nb_chars=200),  # Limiting text length
                client_langue_res=fake.language_name(),
                client_commune=fake.city(),
                client_medref=fake.word(),
                client_cin=fake.random_number(digits=8),
                client_ville=fake.city(),
                client_adresse=fake.address(),
                client_profession=fake.job(),
                client_sexe=fake.random_element(elements=("M", "F")),
                client_provenance=fake.random_element(elements=("A", "B", "C")),
                client_id_externe=fake.random_number(digits=5),
                client_ref_mutuelle_externe=fake.random_number(digits=5),
                client_ref_compte_externe=fake.random_number(digits=5),
            )
            client.save()
        self.stdout.write(self.style.SUCCESS("Fake data populated successfully"))
