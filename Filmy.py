class Movie:
    def __init__ (self, title, year, genre, count_vievs):
        self.title = title
        self.year = year
        self.genre = genre
        self.count_vievs = count_vievs
        
    
    def play(self, vievs=1):    
        self.count_vievs += vievs
        

    def get_movies(self):
        print (self.title, self.year, self.genre, self.count_vievs)
    
class Series(Movie):
    def __init__ (self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

movies = [
        Movie("Mechaniczna Pomarańcza", "1976", "Dramat", 0),
        Movie("Black Jack", "1996", "Sensacyjny", 0),
        Movie("Cierpienia początkującego programisty", "2022", "Dramat psychologiczny", 0),
        Series("S01", "E01", "The Simpsons", "1986", "Sensacyjny", 0),
        Series("S02", "E05", "Uciekające kurczaki", "1986", "Sensacyjny", 0),
        Series("S50", "E99", "Game of Trone", "1986", "Sensacyjny", 0)
]

for i in movies:
    i.play()
    i.get_movies()

