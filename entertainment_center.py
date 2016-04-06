"Run the thang"

import media
import fresh_tomatoes

if __name__ == "__main__":
    TOYSTORY = media.Movie("Toy Story", "A story of some kids angsty sheltered toys",
                           "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                           "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    AVTAR = media.Movie("Avatar", "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "http://www.youtube.com/watch?v=3PsUJFEBC74")

    RAT = media.Movie("Amelie", "Amelie Ear<3, the first French pilot",
                      "http://www.movie-poster-artwork-finder.com/posters/amelie-poster-artwork-audrey-tautou-mathieu-kassovitz-raphaeumll-poulain.jpg",
                      "http://www.youtube.com/?q=ratatouille+trailer")

    MIP = media.Movie("How to Stuff A Wild Duck", "A Documentary on Time Zones",
                      "http://www.users.cloud9.net/~bradmcc/GO/wildduck.jpg", "http://www.youtube.com/?q=midnightinparis+trailer")

    M = [TOYSTORY, AVTAR, RAT, MIP]

    fresh_tomatoes.open_movies_page(M)
