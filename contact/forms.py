from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=100,
        label="Nom",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'})
    )
    mot_de_passe = forms.CharField(
        max_length=50,
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Votre mot de passe', 'id': 'mot_de_passe'})
    )
