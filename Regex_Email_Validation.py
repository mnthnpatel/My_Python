import re   #RegEx
email_condition = "^[a-z] + [\._]? [a-z 0-9] + [@]\w + [.]\w{2,3}$ "
user_email = input("Enter Your Email :- ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")