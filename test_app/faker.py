from app.models import ClientModel
from faker import Faker
import random
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_app.settings")
django.setup()

fake = Faker()

# Function to get a random choice from a tuple
def random_choice(choices):
    return random.choice([choice[0] for choice in choices])


# Create 2000 clients with all fields filled
for _ in range(2000):
    client = ClientModel.objects.create(
        client_num_dossier=fake.random_number(digits=8),
        client_num=fake.random_number(digits=8),
        client_nom=fake.last_name(),
        client_prenom=fake.first_name(),
        client_nom_prenom=fake.name(),
        client_prenom_nom=fake.name(),
        client_mail=fake.email(),
        client_telephone=fake.phone_number(),
        client_type=random_choice(ClientModel.CLIENT_TYPE),
        client_datenaissance=fake.date_of_birth(),
        client_uuid=fake.uuid4(),
        client_code_postale=fake.zipcode(),
        client_language=fake.language_name(),
        client_commentaire=fake.text(max_nb_chars=200),
        client_langue_res=fake.language_name(),
        client_commune=fake.city(),
        client_medref=fake.name(),
        client_cin=fake.random_number(digits=8),
        client_ville=fake.city(),
        client_adresse=fake.address(),
        client_profession=fake.job(),
        client_sexe=random_choice(ClientModel.CLIENT_SEXE),
        client_provenance=random_choice(ClientModel.CLIENT_PROVENANCE),
        client_id_externe=fake.random_number(digits=8),
        client_ref_mutuelle_externe=fake.random_number(digits=8),
        client_ref_compte_externe=fake.random_number(digits=8),
    )

print("2000 clients have been created with all fields filled.")
