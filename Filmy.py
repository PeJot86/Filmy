import random

class Movie:
    def __init__ (self, title, year, genre, count_views):
        self.title = title
        self.year = year
        self.genre = genre
        self.count_views = count_views
        
    def play(self, views=1):    
        self.count_views += views


class Series(Movie):
    def __init__ (self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

database = [
        Movie("Mechaniczna Pomarańcza", "1976", "Dramat", 0),
        Movie("Black Jack", "1996", "Sensacyjny", 0),
        Movie("Cierpienia początkującego programisty", "2022", "Dramat psychologiczny", 0),
        Series("S01", "E01", "The Simpsons", "1986", "Sensacyjny", 0),
        Series("S02", "E05", "Uciekające kurczaki", "1986", "Sensacyjny", 0),
        Series("S50", "E99", "Game of Trone", "1986", "Sensacyjny", 0)
]

def generate_views():
    for _ in range(1, 10):
        view = random.randint(1, 10)
        element = random.choice(database)
        element.play(views=view)

def generate_views_xten ():
    i=0
    while i < 10:
        generate_views()
        i+=1

def get_movies():
    generate_views_xten()
    by_title = sorted(database, key=lambda x: x.title)    
    for element in by_title:
        element.play()
        if not isinstance(element, Series):
            print(f"{element.title}, {element.year}, {element.genre}. Ilość wyświetleń: {element.count_views}.")

def get_series():
    generate_views_xten()
    by_title = sorted(database, key=lambda x: x.title)
    for element in by_title:        
        element.play()        
        if isinstance(element, Series):
            print(f"Serial: {element.title}, {element.year}, {element.genre}, {element.episode}, {element.season}. Ilość wyświetleń: {element.count_views}.")
        
def search ():
    search = input("Podaj tytuł:")
    for element in database:
        if element.title == search:
            print(f"{element.title}, {element.year}, {element.genre}. Ilość wyświetleń: {element.count_views}.")
        break
    else:
        print ("Unknown")

def top_titles():
    generate_views_xten ()
    by_top = sorted(database, key=lambda x: x.count_views)    
    top = by_top[-1]
    print (f"Najpopularniejszy dziś: {top.title}, {top.count_views}")

