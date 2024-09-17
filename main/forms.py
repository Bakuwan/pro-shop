from django.forms import ModelForm
from main.models import ProductEntry

class ProductForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]