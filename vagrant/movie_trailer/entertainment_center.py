import media
import fresh_tomatoes

#create deadpool move instance
deadpool = media.Movie(
    "Deadpool",
    "American superhero film based on the Marvel Comics character Deadpool",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
    "https://www.youtube.com/watch?v=ONHBaC-pfsk")

#create star wars move instance
star_wars = media.Movie(
     "The Force Awakens",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
    "https://www.youtube.com/watch?v=Hyc84zvhbQU")

#create ex machina move instance
ex_machina = media.Movie(
    "Ex Machina",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
    "https://www.youtube.com/watch?v=XYGzRB4Pnq8")

#create the martian movie instance
the_martian = media.Movie(
    "The Martian",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

#create shutter island movie instance
shutter_island = media.Movie(
    "Shutter Island",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

#create fight club movie instance
fight_club = media.Movie(
    "Fight Club",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=J8FRBYOFu2w")

#store move instances in a movies array
movies = [deadpool, star_wars, ex_machina, the_martian, shutter_island, fight_club]

#call open movies page passing the movies array
fresh_tomatoes.open_movies_page(movies)
