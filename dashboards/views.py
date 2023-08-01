from django.shortcuts import render
from residents.models import Municipality, DistrictMunicipality

def dashboard(request):
    municipality_count = Municipality.objects.all().count()
    district_count = DistrictMunicipality.objects.all().count()
    
    context = {
        'municipality_count': municipality_count,
        'district_count': district_count
    }

    return render(request, 'dashboard/dashboard.html', context)
