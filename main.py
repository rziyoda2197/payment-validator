class PaymentValidator:
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def validate_card_number(self):
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            return False
        return True

    def validate_expiration_date(self):
        from datetime import datetime
        expiration_date = datetime.strptime(self.expiration_date, '%m/%y')
        today = datetime.today()
        if expiration_date < today:
            return False
        return True

    def validate_cvv(self):
        if len(self.cvv) != 3 or not self.cvv.isdigit():
            return False
        return True

    def validate_payment(self):
        return self.validate_card_number() and self.validate_expiration_date() and self.validate_cvv()


# Test
payment_validator = PaymentValidator('1234567890123456', '12/30', '123')
print(payment_validator.validate_payment())  # True

payment_validator = PaymentValidator('123456789012345', '12/30', '123')
print(payment_validator.validate_payment())  # False

payment_validator = PaymentValidator('1234567890123456', '01/30', '123')
print(payment_validator.validate_payment())  # False

payment_validator = PaymentValidator('1234567890123456', '12/30', '1234')
print(payment_validator.validate_payment())  # False
