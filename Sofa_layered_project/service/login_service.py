from dao.login_dao import LoginDAO


class LoginService:

    def __init__(self):

        self.login_dao = LoginDAO()


    def login(self, email, password, role):

        if role == "Customer":

            result = self.login_dao.login_customer(
                email,
                password
            )

        elif role == "Admin":

            result = self.login_dao.login_admin(
                email,
                password
            )

        else:

            result = None

        return result