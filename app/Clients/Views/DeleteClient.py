from app.models import ClientModel  # Assuming you have imported the ClientModel
from django.shortcuts import render, redirect
from django.views import View


class DeleteClient(View):
    def get(self, request, client_id):
        client = ClientModel.objects.get(pk=client_id)
        return render(request, "delete_client.html", {"client": client})

    def post(self, client_id):
        client = ClientModel.objects.get(pk=client_id)
        client.delete()
        return redirect("client_list")
