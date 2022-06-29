from django import forms

from wfm.base.models import Item


class DoacaoForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    itens = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)
