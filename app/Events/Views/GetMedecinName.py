from django.http import JsonResponse
from django.views.generic import View
from app.models import MedecinModel

from django.http import JsonResponse
from app.models import MedecinModel

class GetMedecinName(View):
    def get(self, request):
        try:
            search_query = request.GET.get("term", "")
            medecins = MedecinModel.objects.filter(nom__icontains=search_query)
            
            # Create a list of dictionaries containing id and name for each medic
            medecin_data = [{'id': medecin.id, 'name': medecin.nom + " " + medecin.prenom} for medecin in medecins]
            
            return JsonResponse(medecin_data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
