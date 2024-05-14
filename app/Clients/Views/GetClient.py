from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from app.models import ClientModel  # Assuming you have imported the ClientModel


class GetCLient(View):
    def get(self, request):
        try:
            if request.method == "GET":
                # Your logic to retrieve client data
                search_query = request.GET.get("search[value]", "")

                # Query your dataset and filter based on search query
                clients = ClientModel.objects.filter(
                    Q(client_nom__icontains=search_query)
                    | Q(  # Search by client name
                        client_num__icontains=search_query
                    )  # Search by client number
                )
                order_column_index = int(request.GET.get("order[0][column]", 0))
                order_dir = request.GET.get("order[0][dir]", "asc")

                if order_dir == "desc":
                    order_column = list(clients.model._meta.fields)[
                        order_column_index
                    ].name
                else:
                    order_column = (
                        "-" + list(clients.model._meta.fields)[order_column_index].name
                    )

                clients = clients.order_by(order_column)

                # Paginate the filtered results
                paginator = Paginator(
                    clients, 10
                )  # Change '10' to your desired page length
                page_number = int(request.GET.get("start", 0))
                page_length = int(request.GET.get("length", 10))

                # Ensure page_number is always an integer
                page_number = int(page_number) if page_number is not None else 1

                try:
                    # Ensure page_number is always within valid range
                    page_obj = paginator.page(page_number // page_length + 1)

                except EmptyPage:
                    # If the requested page is out of range, return the last page
                    page_obj = paginator.page(paginator.num_pages)

                # Prepare data for DataTables response
                data = {
                    "draw": int(request.GET.get("draw", 1)),
                    "recordsTotal": paginator.count,
                    "recordsFiltered": paginator.count,
                    "data": [
                        {
                            "client_id": client.id,
                            "client_num_dossier": client.client_num_dossier,
                            "client_num": client.client_num,
                            "client_nom": client.client_nom,
                            "client_prenom": client.client_prenom,
                            "client_nom_prenom": client.client_nom_prenom,
                            "client_prenom_nom": client.client_prenom_nom,
                            "client_mail": client.client_mail,
                            "client_telephone": client.client_telephone,
                            "client_type": client.client_type,
                            "client_datenaissance": client.client_datenaissance.isoformat(),
                            "client_uuid": client.client_uuid,
                            "client_code_postale": client.client_code_postale,
                            "client_language": client.client_language,
                            "client_commentaire": client.client_commentaire,
                            "client_langue_res": client.client_langue_res,
                            "client_commune": client.client_commune,
                            "client_medref": client.client_medref,
                            "client_cin": client.client_cin,
                            "client_ville": client.client_ville,
                            "client_adresse": client.client_adresse,
                            "client_profession": client.client_profession,
                            "client_sexe": client.client_sexe,
                            "client_provenance": client.client_provenance,
                            "client_id_externe": client.client_id_externe,
                            "client_ref_mutuelle_externe": client.client_ref_mutuelle_externe,
                            "client_ref_compte_externe": client.client_ref_compte_externe,
                            # Add other client fields as needed
                        }
                        for client in page_obj
                    ],
                }
                return JsonResponse(data)
                # Return JSON response
            else:
                # Handle other HTTP methods (e.g., POST, PUT, DELETE)
                return HttpResponse(status=405)  # Method not allowed

        except Exception as e:
            return JsonResponse(
                {"error": str(e)}, status=500
            )  # Handle other HTTP methods (e.g., POST, PUT, DELETE)
