from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def complete_transaction(self):
        pass


class PayPalGateway(PaymentGateway):

    def connect(self):
        print("Connecting to PayPal...")

    def authorize(self):
        print("Authorizing payment via PayPal...")

    def complete_transaction(self):
        print("Transaction completed using PayPal.")


class StripeGateway(PaymentGateway):

    def connect(self):
        print("Connecting to Stripe...")

    def authorize(self):
        print("Authorizing payment via Stripe...")

    def complete_transaction(self):
        print("Transaction completed using Stripe.")


gateways = [PayPalGateway(), StripeGateway()]

for g in gateways:
    g.connect()
    g.authorize()
    g.complete_transaction()