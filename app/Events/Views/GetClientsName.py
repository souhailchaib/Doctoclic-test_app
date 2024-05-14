from django.http import JsonResponse
from django.views.generic import View
from app.models import ClientModel


class GetClientsName(View):
    def get(self, request):
        try:
            search_query = request.GET.get("term", "")
            clients = ClientModel.objects.filter(client_nom__icontains=search_query)
            client_names = [
                client.client_nom + " " + client.client_prenom for client in clients
            ]
            return JsonResponse(client_names, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
