class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return (
            f"Name: {self.__class__.__name__}(name="
            f"{repr(self.name)}, price={self.price})"
        )
    def __repr__(self):
        return str(self)
        #return f"<Product {self.name!r}>"
    def make_discount(self, discount_percent):
        """
        Applies discount in %

        :param discount_percent
        :return:
        """
        # self.price = self.price *
        self.price *= (100 - discount_percent) / 100

# это просто функция которая ни к чему не привязана.
def apply_discount(product, discount):
    product.price *= (100 - discount) / 100



laptop = Product("Laptop", 2000)
print(laptop.__dict__)
print(laptop)
print(str(laptop))

laptop.make_discount(10)
print(laptop)
# скидываем еще 10%
apply_discount(laptop, 10)
print(laptop)