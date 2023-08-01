# forms.py
'''
from django import forms
from .models import Resident

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'
        # If you want to exclude specific fields, use the 'exclude' attribute instead:
        # exclude = ['photo']
'''
# forms.py

from django import forms
from .models import DistrictMunicipality, Municipality, Village, Household, Resident

class DistrictMunicipalityForm(forms.ModelForm):
    class Meta:
        model = DistrictMunicipality
        fields = '__all__'

class MunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = '__all__'

class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = '__all__'

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = '__all__'

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'

