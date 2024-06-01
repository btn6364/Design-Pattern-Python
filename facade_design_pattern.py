class PayPalGateway: 
    def process_payment(self, amount): 
        return f"Payment of {amount} processed via PayPal."
    
class StripeGateway: 
    def pay(self, amount): 
        return f"Payment of {amount} processed via Stripe."

class CryptoGateway: 
    def make_payment(self, amount): 
        return f"Payment of {amount} processed via Crypto (Bitcoin)."
    
class PaymentFacade: 
    def __init__(self): 
        self.paypal_gateway = PayPalGateway()
        self.stripe_gateway = StripeGateway()
        self.crypto_gateway = CryptoGateway()
    
    def process_payment(self, amount, gateway): 
        if gateway == "paypal":
            return self.paypal_gateway.process_payment(amount)
        elif gateway == "stripe": 
            return self.stripe_gateway.pay(amount)
        elif gateway == "crypto": 
            return self.crypto_gateway.make_payment(amount)
        else: 
            return "Invalid gateway selection."

if __name__=="__main__": 
    payment_facade = PaymentFacade() 

    # Process payments through different gateways 
    print(payment_facade.process_payment(1000, "paypal"))
    print(payment_facade.process_payment(2000, "stripe"))
    print(payment_facade.process_payment(3000, "crypto"))
    print(payment_facade.process_payment(4000, "random_gateway")) 


   
