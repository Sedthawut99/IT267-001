from student import Student

class Itds(Student):
    def __init__(self, stuid, name, major) -> None:
        super().__init__(stuid, name, major)

    def _displayNameAndMajor(self):
        print(f'ITDS Name: {self._stuid}')
        super()._displayNameAndMajor()
        
#create object
stu = Itds("640108","Amorn","Information Technology")
stu._displayNameAndMajor()