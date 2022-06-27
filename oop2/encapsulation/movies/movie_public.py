class Movie:
    #public methods
    def __init__(self) -> None:
        self.title = ''
        self.year = 0
        self.genre = ''

    def add_movie(self,title:str,year:int,genra:str):
        self.title = title
        self.year = year
        self.genre = genra

    def get_movie(self):
        return self.title

if __name__ == '__main__':
    m = Movie()
    #call public method
    m.add_movie('Mulan',2020,'action')
    print(f'Title: {m.get_movie()}')

    #access public attributes -> obj.attribute #บรรทัด 20 23 จะเรียกแบบไหนก็ได้
    print(f'Title: {m.title}')
    print(f'Year: {m.year}')
    print(f'Genre: {m.genre}')