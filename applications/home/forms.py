from django import forms

#
from .models import Suscribers, Contact
class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        """Meta definition for Suscribersform."""
        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder':'Correo Electronico...'
                }
            )
        }

class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""
        model = Contact
        fields = ('__all__')
