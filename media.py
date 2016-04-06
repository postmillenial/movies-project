"Defines the movie class"

class Movie(object):
    "Movie class to store title, synopsis, poster URL and youtube trailer URL"

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
