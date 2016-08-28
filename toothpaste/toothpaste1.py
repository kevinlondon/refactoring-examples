class Shipment:

    LARGE_PACKAGE_PREMIUM = 2
    NORMAL_SHIP_RATE = 1
    BULK_SHIP_RATE = .5

    def __init__(self, items):
        self.items = items

    def get_price(self, items):
        weight_ = sum([item.weight for item in items])
        if weight < 100:
            price = weight * 1
        else:
            price = weight * 1 + 5
        return weight
