from django.db import models

# Create your models here.


class ClientModel(models.Model):

    CLIENT_SEXE = (
        ("1", "Homme"),
        ("0", "Femme"),
        ("2", "Non defini"),
    )

    CLIENT_TYPE = (
        ("1", "EXTERNE"),
        ("0", "INTERNE"),
        ("2", "AUTRE"),
    )

    CLIENT_ETAT_INSCRIPTION = (
        ("0", "ENCOURS"),
        ("1", "CONFIRMEE"),
    )

    CLIENT_ETAT_CHANGEMENT_PWD = (
        ("0", "ENCOURS"),
        ("1", "CONFIRMEE"),
    )

    CLIENT_MAIL_RAP = (
        ("0", "NON"),
        ("1", "OUI"),
    )

    CLIENT_PROVENANCE = (
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("Tiktok", "Tiktok"),
        ("Google", "Google"),
        ("Recommandation patient", "Recommandation patient"),
        ("Recommandation médecin", "Recommandation médecin"),
    )

    client_num_dossier = models.CharField(max_length=500, blank=True, null=True)
    client_num = models.CharField(max_length=500)
    client_nom = models.CharField(max_length=500)
    client_prenom = models.CharField(max_length=500)
    client_nom_prenom = models.CharField(max_length=600, blank=True, null=True)
    client_prenom_nom = models.CharField(max_length=600, blank=True, null=True)
    client_mail = models.CharField(max_length=500, blank=True, null=True)
    client_telephone = models.CharField(max_length=500, blank=True, null=True)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPE, default=2)
    client_datenaissance = models.DateField(blank=True, null=True)

    client_uuid = models.CharField(max_length=600, blank=True, null=True, unique=True)

    client_code_postale = models.CharField(max_length=500, blank=True, null=True)
    client_language = models.CharField(max_length=500, default="Français")
    client_commentaire = models.CharField(max_length=500, blank=True, null=True)

    client_langue_res = models.CharField(max_length=500, default="")
    client_commune = models.CharField(max_length=500, default="")
    client_medref = models.CharField(max_length=500, default="")

    client_cin = models.CharField(max_length=500, blank=True, null=True)
    client_ville = models.CharField(max_length=500, blank=True, null=True)
    client_adresse = models.CharField(max_length=500, blank=True, null=True)
    client_profession = models.CharField(max_length=500, blank=True, null=True)

    client_sexe = models.CharField(max_length=10, choices=CLIENT_SEXE, default=2)
    # client_ref_mutuelle = models.ForeignKey(MutuelleModel, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    client_provenance = models.CharField(
        max_length=100, blank=True, null=True, default=None, choices=CLIENT_PROVENANCE
    )

    client_id_externe = models.CharField(max_length=500, blank=True, null=True)
    client_ref_mutuelle_externe = models.CharField(
        max_length=500, blank=True, null=True
    )
    # client_ref_compte = models.ForeignKey(CompteModel, blank=True, null=True, on_delete=models.CASCADE)
    client_ref_compte_externe = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.client_nom


class CalendarEvent(models.Model):
    # client=models.ForeignKey(ClientModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    all_day = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
