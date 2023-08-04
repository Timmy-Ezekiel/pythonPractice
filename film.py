#the Film class

class Film():
    def __init__(self, filmName, filmId):
        self.filmName = filmName
        self.filmId = filmId
    
    def printDetails(self):
        print(f"The film name is {self.filmName} and it Id is {self.filmId}")
    