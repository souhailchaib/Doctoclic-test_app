from django import forms
from app.models import ClientModel  # Assuming you have imported the ClientModel


class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
