import webbrowser


class Movie():
    """
    Creates an instance of movie with
    title - Movie Title
    storyline - Movie Storline
    poster_image_url - a url to an image
    trailer_youtube_url - a url to a trailer on youtube
	And a method show_trailers to show the trailer in a web browser
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

