# class Album:
    
#     GENRES = ["Hip-Hop", "Pop", "Jazz"]
#     album_count = 0
    
#     def __init__(self, genre,date):
#         if self.check_genre(genre):
#             self.increase_album_count()            
#             self.genre=genre
#             self.release_date = date
            
#     @classmethod
#     def check_genre(cls,genre):
#         return genre in cls.GENRES
    
#     @classmethod
#     def increase_album_count(cls, increment=1):
#          cls.album_count+=increment
#          return cls.album_count
        
# Album("Rap",2001)
# Album("Rap",2002)
# Album("Rap",2003)

# album=Album.GENRES 
# print(album)
# album2=Album.GENRES 
# print(album2)

# Album.GENRES="Not a list anymore"
# album3=Album.GENRES
# print(album3)

# print(Album.increase_album_count())
# print(Album.album_count)

# # Album(2001)
# # Album(2002)
# # Album(2003)

# # album=Album(2024)
# # album.release_date
# # print(album.release_date)

# # album2=Album(2025)
# # album2.release_date
# # print(album.release_date)

# # joshua_tree=Album(2004)
# # joshua_tree.album_count

# # print("Album count :",joshua_tree.album_count)


# # print(Album.album_count)

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza: ({self.ingredients!r})'
    @classmethod
    def margherita(cls):
        return cls (['mozzarella','tomatoes'])
    @classmethod
    def prosciutto(cls):
        return cls (['mozzarella','tomatoes','ham'])

print(Pizza.margherita())
print(Pizza.prosciutto())
