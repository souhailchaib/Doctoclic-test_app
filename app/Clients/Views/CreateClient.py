from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app.Clients.Forms import ClientForm  # Assuming you have imported the ClientForm


class CreateClient(TemplateView):
    def get(self, request):
        form = ClientForm()
        return render(request, "create_client.html", {"form": form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client_list")
        return render(request, "create_client.html", {"form": form})
