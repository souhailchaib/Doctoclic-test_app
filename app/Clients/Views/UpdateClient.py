from django.shortcuts import render, redirect
from django.views import View
from app.models import ClientModel  # Assuming you have imported the ClientModel

from app.Clients.Forms.ClientForm import (
    ClientForm,
)  # Assuming you have imported the ClientForm


class UpdateClient(View):
    def get(self, request, client_id):
        client = ClientModel.objects.get(pk=client_id)
        form = ClientForm(instance=client)
        return render(request, "update_client.html", {"form": form})

    def post(self, request, client_id):
        client = ClientModel.objects.get(pk=client_id)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("client_list")
        return render(request, "update_client.html", {"form": form})
