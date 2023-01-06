import os, json

def get_current_data():
    with open("movie_tv_diary.json") as f:
        titles_data = json.load(f)
        return titles_data

def save_data(data_dict):
    with open("movie_tv_diary.json", 'w') as f:
        json.dump(data_dict, f, indent=2, sort_keys=True)

def get_movies():

    source_dir = input("Enter the full path to the directory holding the movies...\n>>")

    if os.path.isdir(source_dir) and os.path.exists(source_dir):
        print(f"Getting Titles from {os.path.basename(source_dir)}...\nPlease Wait...")

        dir_list = os.listdir(source_dir)
        print(f"Found {len(dir_list)} Titles: ")
        
        count = 1
        for i in dir_list:
            print(f'{count}) {i}')
            count+=1

        main_dict = get_current_data()
        movies_data = main_dict["movies"]
        movies_data = movies_data + dir_list
        main_dict["movies"] = list(set(movies_data))

        save_data(main_dict)

        print(f"Done getting the movie titles, now holding {len(get_current_data()['movies'])} movie titles and {len(get_current_data()['tv-shows'])} tv-shows")

        try_again = input("\n\tRe-Run? (Yes/No) | (1/0)\n>>")

        if try_again.upper() == "YES" or try_again == "1":
            get_movies()
        elif try_again.upper() == "NO" or try_again == "0":
            "Good Bye!!!"
            exit(0)
        else:
            print("invalid option! Good Bye")


    else:
        print(f"It seems the path you Entered is not valid try again :(\n")
        get_movies()


def get_tv():

    source_dir = input("Enter the full path to the directory holding the tv shows...\n>>")

    if os.path.isdir(source_dir) and os.path.exists(source_dir):
        print(f"Getting Titles from {os.path.basename(source_dir)}...\nPlease Wait...")

        dir_list = os.listdir(source_dir)
        print(f"Found {len(dir_list)} Titles: ")
        
        count = 1
        for i in dir_list:
            print(f'{count}) {i}')
            count+=1

        main_dict = get_current_data()
        tv_data = main_dict["tv-shows"]
        tv_data = tv_data + dir_list
        main_dict["tv-shows"] = list(set(tv_data))

        save_data(main_dict)

        print(f"Done getting the Tv-Show titles, now holding {len(get_current_data()['movies'])} movie titles and {len(get_current_data()['tv-shows'])} tv-shows")

        try_again = input("\n\tRe-Run? (Yes/No) | (1/0)\n>>")

        if try_again.upper() == "YES" or try_again == "1":
            get_tv()
        elif try_again.upper() == "NO" or try_again == "0":
            "Good Bye!!!"
            exit(0)
        else:
            print("invalid option! Good Bye")


    else:
        print(f"It seems the path you Entered is not valid try again :(\n")

def main():
    Choice = input("What do you want to do?\n1) Get Movie Titles\n2) Get Tv Show Titles\n3) Exit\n>>")

    try:
        Choice = int(Choice)
    except:
        print("Not A Valid Choice, Try Again"); main()

    if Choice >= 1 and Choice <= 3:
        print(f"You Have Selected Option {Choice}")

        if Choice == 1:
            get_movies()
        elif Choice == 2:
            get_tv()
        elif Choice == 3:
            print("Good Bye")

    else:
        print("Not A Valid Choice, Try Again")
        main()

main()

