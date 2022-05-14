from django import forms
from iteminfo.models import Item, Warehouse, Assignment


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['item_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['item_label'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['item_disambiguator']) == 0:
            result = self.cleaned_data['item_disambiguator']
        else:
            result = self.cleaned_data['item_disambiguator'].strip()
        return result


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

    def clean_assignment_name(self):
        return self.cleaned_data['assignment_name'].strip()


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def clean_warehouse_number(self):
        return self.cleaned_data['warehouse_number'].strip()

    def clean_warehouse_name(self):
        return self.cleaned_data['warehouse_name'].strip()
