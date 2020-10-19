class car():
    """
    Single car object
    """

    def __init__(self, url, price, km):
        self.url = url
        self.price = price.replace(".", "")  # removes the . from 200.000 kr
        self.km = km.replace(".", "")  # removes the . from 85.000 km
        self.price_pr_km = int(
            self.price)/int(self.km) if self.price != "Ring" else "Ring"  # Ternary operation

    def __repr__(self):
        return '\nCar(%r, %r kr, %r km)' % (self.url, self.price, self.km)

    # Whith static we don't need to instanciate the class, to use this method.
    @staticmethod
    def cheapest_pr_km(car_list):
        """
        Calculate what car is the cheapest car pr kilometer
        """
        # We filter out all the cars with "Ring" as a price.
        filtered_cars = filter(lambda x: x.price_pr_km != "Ring", car_list)
        sorted_cars = sorted(filtered_cars, key=lambda x: x.price_pr_km)
        return sorted_cars[0]
