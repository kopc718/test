
users = {"admin": "12345", "admin2": "admin2"}


def login():
    l = [["username", "haslo"]]

    l[0][0] = (input("username: "))
    l[0][1] = (input("password: "))

    try:
        if (users["{l[0][0]}".format(l=l)]) == l[0][1]:
            print("You are logged in")
    except KeyError:
        print("Your username or password is wrong")

login()
