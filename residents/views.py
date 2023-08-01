from django.shortcuts import get_object_or_404, render, redirect 
from .models import DistrictMunicipality, Municipality, Village, Household, Resident
from .forms import *

def district_municipality_list(request):
    districts = DistrictMunicipality.objects.all()
    return render(request, 'district_municipality_list.html', {'districts': districts})

def municipality_list(request):
    municipalities = Municipality.objects.all()
    return render(request, 'municipality_list.html', {'municipalities': municipalities})

def village_list(request):
    villages = Village.objects.all()
    municipalities = Municipality.objects.all()
    context = {
        'villages': villages,
        'municipalities': municipalities
    }
    return render(request, 'village_list.html', context)

def household_list(request):
    households = Household.objects.all()
    return render(request, 'household_list.html', {'households': households})

def create_resident(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resident_list')  
        # Redirect to the resident list page after successful form submission
    else:
        form = ResidentForm()
    return render(request, 'create_resident.html', {'form': form})

def resident_list(request):
    residents = Resident.objects.all()
    return render(request, 'resident_list.html', {'residents': residents})

def details(request, id):
    resident = get_object_or_404(Resident, id=id)
    household = Household.objects.all()

    context = {
        'resident': resident,
        'household': household
    }
    return render(request, 'detail.html', context)

def combined_data_view(request):
    # Query all the residents along with their associated household, 
    # village, municipality, and district.
    residents = Resident.objects.select_related(
        'household__village__town__district'
    ).all()
    # You can now access all the fields from the related models like this:
    context = {
        'residents': residents,
    }
    return render(request, 'combined_data_template.html', context)

def create_district_municipality(request):
    if request.method == 'POST':
        form = DistrictMunicipalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('district_list')
    else:
        form = DistrictMunicipalityForm()
    return render(request, 'create_district_municipality.html', {'form': form})

def create_village(request):
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('village_list')
    else:
        form = VillageForm()
    return render(request, 'create_village.html', {'form': form})

def create_municipality(request):
    if request.method == 'POST':
        form = MunicipalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('village_list')
    else:
        form = MunicipalityForm()
    return render(request, 'create_municipality.html', {'form': form})