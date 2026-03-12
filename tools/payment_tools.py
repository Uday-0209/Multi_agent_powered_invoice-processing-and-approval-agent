class PaymentTools:

    def verify_payment(self, receipt_amount, invoice_amount):

        if receipt_amount != invoice_amount:

            return {
                "status": "invalid",
                "reason": "Payment mismatch"
            }

        return {
            "status": "valid"
        }