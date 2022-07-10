class Donkey:

    def __init__(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print('Donkey makes eeyore sound')

    def show_info(self):
        print('***** Meme Info *****')
        print(f'Age: {self.age}')
        print(f'Weight: {self.weight}')
    