import fresh_tomatoes
import Media

logan = Media.Movie("Logan",
                    "In the near future, a weary Logan cares for an ailing Professor X somewhere on the Mexican border. However, Logan's attempts to hide from the world and his legacy are upended when a young mutant arrives, pursued by dark forces.",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")


titanic=Media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")


avatar = Media.Movie("Avatar",
                     " A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


it = Media.Movie("It",
                 "In a small town of Derry, Maine, seven children come face to face with life problems, bullies and a monster that takes the shape of a clown called Pennywise",
                 "https://upload.wikimedia.org/wikipedia/en/a/a2/It_%282017%29_logo.jpg",
                 "https://www.youtube.com/watch?v=FnCdOQsX5kc")


the_persuit_of_happyness = Media.Movie("The Persuit of Happyness",
                                       "A struggling salesman takes custody of his son as he's poised to begin a life-changing professional endeavor.",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                       "https://www.youtube.com/watch?v=89Kq8SDyvfg")

the_shawshank_redemption = Media.Movie("The Shawshank Redemption",
                            "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                            "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                            "https://www.youtube.com/watch?v=6hB3S9bIaco")

movies = [logan, titanic,  avatar, it, the_persuit_of_happyness, the_shawshank_redemption,]
fresh_tomatoes.open_movies_page(movies)

#print(avatar.storyline)
#avatar.show_trailer()

#the_shawshank_redemption.show_trailer()
