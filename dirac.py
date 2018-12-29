favorite_movie = "Snatch"
favorite_song = "We built this city"
favorite_food = "Steak"
faves = ({"Favorite Movie" : favorite_movie, "Favorite Song" : favorite_song, "Favorite Food": favorite_food})
faves["Favorite Food"]
for fave in faves.keys():
    print(fave + " : "  + faves[fave])

least_favorite_movie = "Godfather"
least_favorite_song = "It's a small world"
least_favorite_food = "Beats"
least_faves = ({"Least favorite Movie" : least_favorite_movie, "Least Favorite Song" : least_favorite_song, "Least Favorite Food" : least_favorite_food})
for least_fave in least_faves.keys():
    print(least_fave + " : "  + least_faves[least_fave])

prefrences = (faves, least_faves)  
def pref():
    for fave in faves.keys():
        print(fave + " : "  + faves[fave]) 
    for least_fave in least_faves.keys():
        print(least_fave + " : "  + least_faves[least_fave])