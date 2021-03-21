from applications.home.models import Home

#Procesor para recuperar correo y telefono desde HOME
def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'correo': home.contac_email,
    }