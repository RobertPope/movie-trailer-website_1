import fresh_tomatoes
import media

# Create my listing of movie objects
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy with creepy toys",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://youtu.be/KYz2wyBy3kc"
)

avatar = media.Movie(
    "Avatar",
    "A Marine on an alean planet",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/5PSNL1qE6VY"
)

iron_man = media.Movie(
    "Iron Man",
    "A Man in a can with a plan",
    "http://vignette3.wikia.nocookie.net/marvelmovies/images/0/04/Iron_Man_artposter.jpg/revision/latest?cb=20140203181914",
    "https://youtu.be/8hYlB38asDY"
)

school_of_rock = media.Movie(
    "School of Rock",
    "A quitar a man and his dream",
    "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
    "https://youtu.be/XCwy6lW5Ixc"
)

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "A nite in the city of love",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://youtu.be/FAfR8omt-CY"
)

hunger_games = media.Movie(
    "Hunger Games",
    "A girl with a temper and a bow",
    "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SX640_SY720_.jpg",
    "https://youtu.be/FovFG3N_RSU"
)

movies = [toy_story, avatar, iron_man, school_of_rock, midnight_in_paris, hunger_games]

# Pass movies to the fresh tomotoes script to generate static HTML page

fresh_tomatoes.open_movies_page(movies)
