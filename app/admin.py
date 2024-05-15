from django.contrib import admin
from app.models import ClientModel
from .models import MedecinModel

admin.site.register(MedecinModel)



@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "client_num_dossier",
        "client_num",
        "client_nom",
        "client_prenom",
        "client_nom_prenom",
        "client_prenom_nom",
        "client_mail",
        "client_telephone",
        "client_type",
        "client_datenaissance",
        "client_uuid",
        "client_code_postale",
        "client_language",
        "client_commentaire",
        "client_langue_res",
        "client_commune",
        "client_medref",
        "client_cin",
        "client_ville",
        "client_adresse",
        "client_profession",
        "client_sexe",
        "client_provenance",
        "client_id_externe",
        "client_ref_mutuelle_externe",
        "client_ref_compte_externe",
    )
    list_filter = (
        "client_num_dossier",
        "client_num",
        "client_nom",
        "client_prenom",
        "client_nom_prenom",
        "client_prenom_nom",
        "client_mail",
        "client_telephone",
        "client_type",
        "client_datenaissance",
        "client_uuid",
        "client_code_postale",
        "client_language",
        "client_commentaire",
        "client_langue_res",
        "client_commune",
        "client_medref",
        "client_cin",
        "client_ville",
        "client_adresse",
        "client_profession",
        "client_sexe",
        "client_provenance",
        "client_id_externe",
        "client_ref_mutuelle_externe",
        "client_ref_compte_externe",
    )
    search_fields = (
        "client_num_dossier",
        "client_num",
        "client_nom",
        "client_prenom",
        "client_nom_prenom",
        "client_prenom_nom",
        "client_mail",
        "client_telephone",
        "client_type",
        "client_datenaissance",
        "client_uuid",
        "client_code_postale",
        "client_language",
        "client_commentaire",
        "client_langue_res",
        "client_commune",
        "client_medref",
        "client_cin",
        "client_ville",
        "client_adresse",
        "client_profession",
        "client_sexe",
        "client_provenance",
        "client_id_externe",
        "client_ref_mutuelle_externe",
        "client_ref_compte_externe",
    )

