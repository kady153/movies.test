import media
import fresh_tomatoes
interstellar=media.Movie("Interstellar","a mission to search for a new home in space",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
	"https://www.youtube.com/watch?v=zSWdZVtXT7E")
black_panther=media.Movie("Black panther","a story of a knig trying to protect his home",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcQPpcKQ9eWZGxJe6eXyCW91eayLVm4KqruvJz3GP0F2T2w46yKZ",
	"https://www.youtube.com/watch?v=xjDjIWPwcPU")

get_out=media.Movie("Get out","a young man observe strange things on his trip",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcz1F_gt1m1jGN_Es_3g2xSeu5ToB2QCLgthES8elZgJhVi0CxR_27jA",
	"https://www.youtube.com/watch?v=sRfnevzM9kQ")

shawshank_redemption=("The shawshank redemption","Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDcd8ZZ7QOIQgvR_CcZAn4sVPgIOS4NbETLATZO36MEH5yOTOP13z28Q",
	"https://www.youtube.com/watch?v=6hB3S9bIaco")
passengers=media.Movie("passengers","a man on his trip in space found himself awake earlier than the ship arrives its destination",
	"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ12eOGpcmAlpqo4oX2ReVrteNW6k_EaC2ej3mN801PSNEHEpECxYDBg",
	"https://www.youtube.com/watch?v=7BWWWQzTpNU")

movies=[interstellar,black_panther,get_out,shawshank_redemption,passengers]
fresh_tomatoes.open_movies_page(movies)
print get_out.storyline
get_out.show_trailer()