class Order:

    MAX_PROMO_CODES = 3

    def __init__(self, items, promo_codes):
        self.items = items
        self.promo_codes = promo_codes

    @property
    def promo_codes(self):
        return self._promo_codes

    @promo_codes.setter
    def promo_codes(self, code):
        self._promo_codes = []
        if code.is_valid() and len(self._promo_codes) < Order.MAX_PROMO_CODES:
            self._promo_codes.append(code)

    def calculate_total(self):
        total = sum([item.price for item in items])
        for promo_code in self.promo_codes:
            total -= promo_code.value

        return total
