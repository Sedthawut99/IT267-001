class ABank:
    def __init__(self,loanamount:int,loanyear:int,loanrate:float,interest:float,monthlypay:float) -> None:
        self.__loanamount = loanamount
        self.__loanyear = loanyear
        self.__loanrate = loanrate
        self.interest = interest
        self.monthlypay = monthlypay

    def flat_rate(self):
        pass

    def display_interest(self):
        pass