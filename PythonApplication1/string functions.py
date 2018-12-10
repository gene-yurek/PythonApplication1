

user_name = input ("please enter your name\n")
c = user_name.find(",")
s = user_name.find(" ")

if c > 0:
    print("Your last name is " + user_name[0:c].strip())
    print("Your first name is " + user_name[c+1:len(user_name)].strip())
else:
    print("Your first name is " + user_name[0:s].strip())
    print("Your last name is " + user_name[s:len(user_name)].strip())

