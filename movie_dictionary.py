def add_or_update_a_movie(movie_dict, movie_name, actors):
    if movie_name not in movie_dict:
        movie_dict[movie_name] = actors
    else:
        existing_actors = movie_dict[movie_name]
        existing_actors.extend(actors)
        final = []
        for name in existing_actors:
            if name not in final:
                final.append(name)
        movie_dict[movie_name]= final
    return movie_dict


def remove_actor_from_movie(movie_dict, movie_name, actor):
    for key in movie_dict:
        current_actors = movie_dict[key]
        if actor in current_actors:
            current_actors.remove(actor)
    return movie_dict


def find_movie_with_most_actors(movie_dict):
    most_actors = 0
    for key in movie_dict:
        actors_list = movie_dict[key]
        if (len(actors_list) > most_actors) :
            most_actors = len(actors_list)
            final_movie = key
    return final_movie


def find_similar_movies(movie_dict, actor1, actor2):
    final = []
    for key in movie_dict:
        actors_list = movie_dict[key]
        if ((actor1 in actors_list) and (actor2 in actors_list)):
            final.append(key)
    return final


def find_actor_with_most_movies(movie_dict):
    all_actors = []
    for key in movie_dict:
        actors_list = movie_dict[key]
        all_actors.extend(actors_list)
    highest_count = 0
    for actor in all_actors:
        appearances = all_actors.count(actor)
        if (appearances > highest_count):
            highest_count = appearances
            final_actor = actor
    return final_actor
