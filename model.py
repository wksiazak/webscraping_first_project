# obiekty klasy modelu - determinuje strukturę danych

class top250:
    def __init__(self, title, year, director, stars,  rating, link):
        self.title = title
        self.year = year
        self.director = director
        self.stars = stars
        self.rating = rating
        self.link = link
    def __str__ (self):
        return '| %100s | %5s | %50s | %100s | %5s | %50s |'% \
               (self.title, self.year, self.director, self.stars,  self.rating, self.link)