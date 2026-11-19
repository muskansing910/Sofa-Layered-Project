from dao.admin_dao import Admin_dao


class Admin_service:

    def display_admins(self):

        dao = Admin_dao()

        admins = dao.display_all()

        return admins