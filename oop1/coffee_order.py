class CoffeeOrder :
    menu_type = "Coffee"
    total = "0"
    def __init__(self,customer_name:str,menu:str,price:float,num:int = "1",size:str = "R") -> None:
        self.customer_name = customer_name
        self.menu = menu
        self.num = num
        self.size = size  
        self.price = price

    def check_menu(menu):
        menu= menu.upper()
        if menu == 'CM':
            return  'Cafe Mocha'
        elif menu == 'CP':
            return 'Cappuccino'
        elif menu == 'AM':
            return 'Americano'
        elif menu == 'CL':
            return 'Cafe Latte'
        elif menu == 'VL':
            return 'Vanilla Latte'
        elif menu == 'ES':
            return 'Espresso'


    def compute_price(self):
        pass

    def display_detail(self):
        pass