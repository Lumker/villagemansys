from django.db import models

class DistrictMunicipality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(DistrictMunicipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Village(models.Model):
    name = models.CharField(max_length=100)
    town = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Household(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    has_electricity = models.BooleanField(default=False)
    has_water = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)  # Address field placed in Household model

    def __str__(self):
        return f"Household in {self.village}"

class Resident(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    EMPLOYMENT_CHOICES = (
        ('EMP', 'Employed'),
        ('UNEMP', 'Unemployed'),
        ('STUD', 'Student'),
        ('RETIRED', 'Retired'),
        ('OTHER', 'Other'),
    )

    id_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images', null=True)
    cellphone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    employment_status = models.CharField(max_length=10, choices=EMPLOYMENT_CHOICES, default='UNEMP')

    def __str__(self):
        return f"{self.name} {self.surname}"
