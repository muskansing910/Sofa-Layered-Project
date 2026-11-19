from service.login_service import LoginService


service = LoginService()

email = input("Enter email: ")
password = input("Enter password: ")
role = input("Enter role (Customer/Admin): ")


result = service.login(email, password, role)


if result:

    print("Login successful")
    print("ID:", result[0])
    print("Name:", result[1])

else:

    print("Invalid email or password")