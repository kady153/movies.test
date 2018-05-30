import media
import fresh_tomatoes


# movies and their information (name,storyline,posterimage,trailer)
interstellar = media.Movie("Interstellar",
                           "a mission to search for a newhome in space",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

black_panther = media.Movie("Black panther",
                            "a story of a knig trying toprotect his home",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQPpcKQ9eWZGxJe6eXyCW91eayLVm4KqruvJz3GP0F2T2w46yKZ",  # NOQA
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

django_unchained = media.Movie("Django Unchained",
                      "with the help of his mentor a slave trned into bounty\
                       hunter and sets off to rescue his wife",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcSnm2FczCxSnt69XUZqqI5-sfy66SvjiV0du9mfUKRRCGqVAurt",  # NOQA
                      "https://www.youtube.com/watch?v=eUdM9vrCbow")

shawshank_redemption = media.Movie("The shawshank redemption",
                                   "Two imprisoned men bond over a number of\
                                    years, finding solace and eventual \
                                    redemption through acts of common decency",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",  # NOQA
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")  # NOQA


passengers = media.Movie("passengers",
                         "a man on his trip in space found himself awake\
                          earlier than the ship arrives its destination",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQvqid_\
                          rbEby5j_XkVnSdwWgvSTiX9Np1I6iTJPJWYZFCBOPe4w",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

movies = [interstellar, black_panther,
          django_unchained, shawshank_redemption, passengers]
          
# creates a webbpage with the movies we have chosen
fresh_tomatoes.open_movies_page(movies)
