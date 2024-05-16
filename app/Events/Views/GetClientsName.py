from django.http import JsonResponse
from django.views.generic import View
from app.models import ClientModel


class GetClientsName(View):
    def get(self, request):
        try:
            search_query = request.GET.get("term", "")
            clients = ClientModel.objects.filter(client_nom__icontains=search_query)
            # Create a list of dictionaries containing id and name for each client
            client_data = [
                {
                    "id": client.id,
                    "name": client.client_nom + " " + client.client_prenom,
                }
                for client in clients
            ]

            return JsonResponse(client_data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
