import random

def list_movies(movies_db):
    print(f'{len(movies_db)} movies in total')
    for key, value in movies_db.items():
        print(f'{key}: {value}')
    input("\nPress Enter to continue ")

def add_movie(movies_db):
    movie_to_be_added = input('Enter new movie name: ')
    try:
        movie_rating = float(input('Enter new movie rating (0-10): '))
        if 0 <= movie_rating <= 10:
            movies_db[movie_to_be_added] = movie_rating
            print(f'Movie {movie_to_be_added} successfully added')
        else:
            print('Rating must be between 0 and 10.')
    except ValueError:
        print('Invalid rating! Please enter a number between 0 and 10.')
    input("\nPress Enter to continue ")

def delete_movie(movies_db):
    movie_to_be_deleted = input('Enter movie name to delete: ')
    if movie_to_be_deleted in movies_db:
        del movies_db[movie_to_be_deleted]
        print(f'Movie {movie_to_be_deleted} successfully deleted')
    else:
        print(f"Movie {movie_to_be_deleted} doesn't exist!")
    input("\nPress Enter to continue ")

def update_movie(movies_db):
    movie_name = input('Enter movie name: ')
    if movie_name in movies_db:
        try:
            new_rating = float(input('Enter new movie rating (0-10): '))
            if 0 <= new_rating <= 10:
                movies_db[movie_name] = new_rating
                print(f'Movie {movie_name} successfully updated')
            else:
                print('Rating must be between 0 and 10.')
        except ValueError:
            print('Invalid rating! Please enter a number between 0 and 10.')
    else:
        print(f"Movie {movie_name} doesn't exist!")
    input("\nPress Enter to continue ")

def stats(movies_db):
    values = list(movies_db.values())
    if not values:
        print('No movies in the database to calculate stats.')
        input("\nPress Enter to continue ")
        return

    average = round(sum(values) / len(values), 2)
    sorted_values = sorted(values)
    length_of_sorted_values = len(sorted_values)

    if length_of_sorted_values % 2 == 0:
        median = (sorted_values[length_of_sorted_values // 2 - 1] + sorted_values[length_of_sorted_values // 2]) / 2
    else:
        median = sorted_values[length_of_sorted_values // 2]

    max_key = max(movies_db, key=movies_db.get)
    min_key = min(movies_db, key=movies_db.get)

    print(f'Average Rating: {average}')
    print(f'Median Rating: {median}')
    print(f'Best Movie: {max_key} ({movies_db[max_key]})')
    print(f'Worst Movie: {min_key} ({movies_db[min_key]})')
    input("\nPress Enter to continue ")

def random_movie(movies_db):
    if movies_db:
        random_key, random_value = random.choice(list(movies_db.items()))
        print(f"Your movie for tonight: {random_key}, it's rated {random_value}")
    else:
        print("No movies in the database!")
    input("\nPress Enter to continue ")

def search_movie(movies_db):
    movie_to_search = input('Enter part of movie name: ').lower()
    results = [(key, value) for key, value in movies_db.items() if movie_to_search in key.lower()]
    if results:
        for key, value in results:
            print(f'{key}: {value}')
    else:
        print(f'{movie_to_search} not found in the database.')
    input("\nPress Enter to continue ")

def sorted_movie(movies_db):
    sorted_items = sorted(movies_db.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        print(f'{key}: {value}')
    input("\nPress Enter to continue ")

def main():
    print('********** My Movies Database **********')
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    while True:
        print('Menu:')
        print('0. Exit')
        print('1. List movies')
        print('2. Add movie')
        print('3. Delete movie')
        print('4. Update movie')
        print('5. Stats')
        print('6. Random movie')
        print('7. Search movie')
        print('8. Movies sorted by rating')
        print('9. Exit')

        try:
            choice = int(input('Enter choice (0-9): '))
            if choice == 0:
                print('Bye')
                break
            elif choice == 1:
                list_movies(movies)
            elif choice == 2:
                add_movie(movies)
            elif choice == 3:
                delete_movie(movies)
            elif choice == 4:
                update_movie(movies)
            elif choice == 5:
                stats(movies)
            elif choice == 6:
                random_movie(movies)
            elif choice == 7:
                search_movie(movies)
            elif choice == 8:
                sorted_movie(movies)
            else:
                print('Invalid choice. Please select between 1 and 9.')
        except ValueError:
            print('Invalid input! Please enter a number between 1 and 9.')
            #hey this is a new comment

if __name__ == "__main__":
    main()
