from random import randint


"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty, tax, order_type):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_base_price(self):
        """Get a random integer to make Splurge pricing."""

        return randint(5, 9)


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            # base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * (base_price * 1.5)
        else:    
            total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        # over write the attributes of parent class with attributes that
        # only apply to DomesticMelonOrder class.
        super(DomesticMelonOrder, self).__init__(species, qty, .08, "domestic")




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, .17, "international")

        self.country_code = country_code

        
    def get_total(self):
        """Calculate price for quantities of less than 10 melons. """

        sub_total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total = sub_total + 3.00
        else:
            total = sub_total
        return total        


    def get_country_code(self):
        """Return the country code."""

        return self.country_code




class GovernmentMelonOrder(AbstractMelonOrder):
    """Changes tax amount for government orders and requires inspection."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty, 0)

        self.passed_inspection = False


    def mark_inspection(self, passed):
        self.passed_inspection = passed

