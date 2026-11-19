from dao.sofa_type_dao import SofaType_dao


class SofaType_service:

    def add_sofa_type(self, sofa_type):
        dao = SofaType_dao()
        dao.add_sofa_type(sofa_type)


    def display_sofa_types(self):
        dao = SofaType_dao()
        sofa_types = dao.display_all()
        return sofa_types

    def display_active_sofa_types(self):

        dao = SofaType_dao()

        sofa_types = dao.display_active_sofa_types()

        return sofa_types