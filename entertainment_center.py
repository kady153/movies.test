import media
import fresh_tomatoes


# movies and their information
interstellar = media.Movie("Interstellar",
                           "a mission to search for a newhome in space",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mk\
                            er2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

black_panther = media.Movie("Black panther",
                            "a story of a knig trying toprotect his home",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQPpcK\
                             Q9eWZGxJe6eXyCW91eayLVm4KqruvJz3GP0F2T2w46yKZ",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

get_out = media.Movie("Get out",
                      "a young man observe strange things onhis trip",
                      "https://movies.universalpictures.com/media/get-out-main-one-sheet-58753d5968ead-1.png",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

shawshank_redemption = media.Movie("The shawshank redemption",
                                   "Two imprisoned men bond over a number of\
                                    years, finding solace and eventual \
                                    redemption through acts of common decency",
                                   "http://t0.gstatic.com/images?q=tbn:\
                                   ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_\
                                   mImChPuMrunA1XjNTSKm",
                                   "https://www.youtube.com/watch?v=\
                                   6hB3S9bIaco")


passengers = media.Movie("passengers",
                         "a man on his trip in space found himself awake\
                          earlier than the ship arrives its destination",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQvqid_\
                          rbEby5j_XkVnSdwWgvSTiX9Np1I6iTJPJWYZFCBOPe4w",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU")

movies = [interstellar, black_panther,
          get_out, shawshank_redemption, passengers]
fresh_tomatoes.open_movies_page(movies)
