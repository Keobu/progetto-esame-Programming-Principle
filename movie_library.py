import json 
from collections import Counter
class MovieNotFoundError(Exception):
    pass


class MovieLibrary:
    def __init__(self, json_file):
        self.json_file = json_file
        try:
            with open(self.json_file, "r") as file:
                self.movies = json.load(file)
            print(f"file {self.json_file} uploaded successfully.") 
        #esercizio 17 modifica del metodo costruttore nel caso di file non trovati 
        except FileNotFoundError:
            raise FileNotFoundError(f"File not Found: {self.json_file}") 
    def _update_json_file(self):
        with open(self.json_file, "w") as file:
            json.dump(self.movies, file, indent=4)
            print(f"file {self.json_file} has been updated.")

#esercizio 1 metodo per restituire l'intera collezione 
    def get_movies(self):
        return self.movies
    
#esercizio 2 metodo per agiungere un nuovo film
    def add_movie(self, title, director, year, genres): 
        new_movie = {
            "title": title,
            "director": director,
            "year": year,
            "genres": genres
        }
        self.movies.append(new_movie)
        
        self._update_json_file()

#esercizio 3 metodo per rimuovere un film 
#esercizio 18 modifica del metodo nel caso non viene trovato nessun file 
    def remove_movie(self, title):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self._update_json_file()
                print("film removed")
                return movie
        raise MovieNotFoundError("Movie was not Found")
    
#esercizio 4 metodo per agiornare un film e restituire il fil aggiornato 
#esercizio 18 modifica del metodo nel caso non viene trovato nessun file 
    def update_movie(self, title, director=None, year=None, genres=None):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                if director:
                    movie["director"] = director
                if year:
                    movie["year"] = year
                if genres:
                    movie["genres"] = genres
                self._update_json_file()
                return movie
        raise MovieNotFoundError("Movie was not Found")
    
#esercizio 5 metodo che restituisce una lista con tutti i titolidei film 
    def get_movie_titles(self):
        return [movie["title"] for movie in self.movies]
    
#esercizio 6 metodo che restituisce il numero totale dei film nella collezione 
    def count_movies(self):
        return len(self.movies)

#esercizio 7 metodo che restituisce il film in base al titolo 
    def get_movie_by_title(self, title):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie 
        raise ModuleNotFoundError("Movie wasn't found")

#esercizio 8 metodo che restituisce uan lista di film che contengon nel titolo una sottostringa 
    def get_movies_by_title_substring(self, substring):
        return [
            movie for movie in self.movies
            if substring in movie["title"]
        ]

#esercizio 9 metodo che restituisce una lista di film in base all'anno 
    def get_movies_by_year(self, year):
       return [
           movie for movie in self.movies
           if movie["year"] == year
       ]

#esercizio 10 metodo che restituisce una lista di film in base al director
    def count_movies_by_director(self, director):
        return sum(
            1 for movie in self.movies
            if movie["director"].lower() == director.lower()
        )

#esercizio 11 metodo che restituisce una lista di film in base al genere 
    def get_movies_by_genre(self, genre):
        return [
            movie for movie in self.movies
            if any(g.lower() == genre.lower() for g in movie["genres"])
        ]

#esercizio 12 metodo che restituisce il titolo del film antico della collezione 
    def get_oldest_movie_title(self):
        if not self.movies:
            raise ValueError("the collection is empty")
        oldest_movie = min(self.movies, key=lambda movie: movie["year"])
        return oldest_movie["title"]

#esercizio 13 metodo che restituisce una media aritmetica degli anni di pubblicazione 
    def get_average_release_year(self):
        if not self.movies:
            raise ValueError
        years = [movie["year"] for movie in self.movies]
        average = sum(years)/len(years)
        return average

#esercizio 14 metodo che restituisce il titolo più lungo della collezione film
    def get_longest_title(self):
        if not self.movies:
            raise ValueError
        longest_movie = max(self.movies, key=lambda movie: len(movie["title"]))
        return longest_movie["title"]

#esercizio 15 il metodo che restituisce una lista contenente i titoli
    def get_titles_between_years(self, start_year, end_year):
        return [
            movie["title"] for movie in self.movies
            if start_year <= movie["year"] <=end_year
        ]

#esercizio 16 metodo che restituisce l'anno che si ripete più spesso fra i film 
    def get_most_common_year(self):
        if not self.movies:
            raise ValueError ("The collection is empty, impossible to determine the most common year.")
        years = [movie["year"] for movie in self.movies]
        year_counts = Counter(years)

        most_common_year = max(year_counts, key=year_counts.get)
        return most_common_year

