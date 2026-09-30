#The programm stores a correct username and a correct password.
#The programm asks the user to enter a username.
#The programm asks the user to enter a password.
#The programm checks whether the entered username matches the stored username.
#The programm checks whether the entered password matches the stored password.
#If both the username and password are correct, the programm allows access.
#Otherwise, gthe programm denies access.

correct_username = "harry"
correct_password = "potter"

username = input("Enter your username: ")
password = input("Enter your password: ")

#if username == correct_username and password == correct_password:
#   print(f"Welcome to Hogwarts, {username} {password}!")
#else:
#  print(f"Accses denied. Go away, {username}!")

if username != correct_username or password != correct_password:
    print(f"Accses denied. Go away, {username}!")
else:
    print(f"Welcome to Hogwarts, {username} {password}!")
    