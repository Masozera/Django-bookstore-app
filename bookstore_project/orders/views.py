from django.views.generic.base import TemplateView
from django.conf import settings # new comes along with the publishable key wc is gonna be set tp context
from django.contrib.auth.models import Permission # new This will eneble the specialUser with password mugaboadmam to view the books after payment

import stripe # new
from django.shortcuts import render # new

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

# We have used the publishable key to send the credit
# card information to Stripe, and Stripe has sent us back a unique token for the order.
# But we haven’t used that token yet to make a charge! Recall that we send an order
# form to Stripe with the Publishable Key, Stripe validates it and sends back a token,
# and then we process the charge using both the token and our own Secret Key.

def charge(request): # new
    # Get the permission
    permission = Permission.objects.get(codename='special_status')
    # Get user
    u = request.user
    # Add to user's permission set
    u.user_permissions.add(permission)





    if request.method == 'POST':
        charge = stripe.Charge.create(
        amount=3900,
        currency='usd',
        description='Purchase all books',
        source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')
# Create a charge view
#  that receives the token from Stripe, makes the charge, and then redirects to the
# charge page upon success.

