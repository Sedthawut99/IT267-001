from horse import Horse
from donkey import Donkey
class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str,age:int,weight:float) -> None:
        super().__init__(name, color,age,weight)

    def run(self):
        print("Mule is running")

    def show_info(self):
        super().show_info

if __name__ == "__main__":

    mule1 = Mule('Mumu','Blue-eyed cream',3,200)
    

