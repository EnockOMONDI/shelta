from django import forms


class CompanyProfileRequestForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email address',
                'class': 'form-control',
            }
        )
    )
