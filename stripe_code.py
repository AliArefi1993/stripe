import stripe

# Set your Stripe API secret key (you can get this from the Stripe dashboard)
stripe.api_key = "sk_test_51NYOY4GxKyXTWdYlJHUFTKUeT5snJRl6P13zp0rJtNVOMrhtWuMhAVfFj39NwQluUyaupjlg6UJhkfQdyjvKIOsa00sERRraUy"


def create_customer(email, source_token):
    # Create a new customer in Stripe
    customer = stripe.Customer.create(
        email=email,
        # The credit card token generated by the Stripe.js or Elements client-side library
        source=source_token
    )
    return customer


def charge_customer(customer_id, amount, currency='usd'):
    # Charge the customer's credit card
    charge = stripe.Charge.create(
        customer=customer_id,
        amount=amount,
        currency=currency,
        description='Example Charge'
    )
    return charge


# Example usage:
try:
    # Create a new customer
    # 'tok_visa' is a test token for a Visa card
    customer = create_customer('customer@example.com', 'tok_visa')

    # Charge the customer $10 (in cents)
    charge = charge_customer(customer.id, 1000)

    # Print the charge details
    print(f"Charge ID: {charge.id}")
    print(f"Amount Charged: {charge.amount} {charge.currency}")
    print(f"Payment Status: {charge.status}")

except stripe.error.StripeError as e:
    # Handle any Stripe API errors
    print(f"Error: {e.user_message}")
