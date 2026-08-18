# Strategy Pattern - Payment Processing System

# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategy 1: Credit Card
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


# Concrete Strategy 2: PayPal
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


# Concrete Strategy 3: Bitcoin
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin.")


# Context
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_payment_method(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
print("Payment Processing System")
print("1. Credit Card")
print("2. PayPal")
print("3. Bitcoin")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: ₹"))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = PayPalPayment()
elif choice == 3:
    strategy = BitcoinPayment()
else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)