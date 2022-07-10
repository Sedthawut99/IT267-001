class JuiceOrder:
    total = 0
    num = 1
    def __init__(self,menu:str,size:str,price:int) -> None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'LJ':25,
            'PJ':30
        }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'R':
            self.price += 0
        elif self.size == 'L':
            self.price += 5

        JuiceOrder.total = self.num * self.price

    def display_order(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu} ({self.size} * {self.price}) => {JuiceOrder.total} baht'

if __name__ == "__main__":

    order1 = JuiceOrder('WJ','L',35 )
    order2 = JuiceOrder('OJ','R',25 )
    order3 = JuiceOrder('PJ','L',35 )

    print(order1.display_order())
    print(order2.display_order())
    print(order3.display_order())