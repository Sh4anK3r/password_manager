import json
from prettytable import PrettyTable

ENTRY_PASSWORD = "123456"

entry = input("Enter password to entry: ")

def add_password(website, username, password):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = []

    data.append(
        {
            "Website": website, 
            "Username": username,
            "Password": password,   
        }    
    )
    
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

def check_password():
    tabel = PrettyTable()
    tabel.field_names = ["Website", "Username", "Password"]

    with open("data.json", "r") as r:
        dane = json.load(r)

    for data in dane:
        tabel.add_row([data['Website'], data['Username'], data['Password']])

    print(tabel)

def delete_password(d_website):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print("The data.json file does not exist.")
        return
    
    for i, entry in enumerate(data):
        if entry["Website"] == d_website:
            del data[i]
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            print(f"Data for the website {d_website} has been deleted.")
            return
    print(f"No data found for the website {d_website}.")


def main():

    while True:
        if entry == ENTRY_PASSWORD:
            choice = input("What do u want to do: (c to check, a to add, q to quit, d to delete): ").lower()
            if choice == "q":
                print("!Goodbye!")
                break
            elif choice == "c":
                check_password()
            elif choice == "a":
                website = input("Enter the website for which you want to save the password: ")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if not website or not username or not password:
                    print("Invalid data!")
                else:
                    add_password(website, username, password)
            elif choice == "d":
                d_website = input("Enter the website for which you want to delete data: ")
                delete_password(d_website)

            else:
                print("Invalid value!")    


if __name__ == "__main__":
    main()