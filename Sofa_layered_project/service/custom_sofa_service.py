from dao.custom_sofa_dao import CustomSofa_dao


class CustomSofa_service:

    def add_custom_sofa(self, custom_sofa):

        dao = CustomSofa_dao()

        dao.add_custom_sofa(custom_sofa)


    def display_custom_sofas(self):

        dao = CustomSofa_dao()

        custom_sofas = dao.display_all()

        return custom_sofas


    def search_custom_sofa_by_id(self, id):

        dao = CustomSofa_dao()

        custom_sofa = dao.display_by_id(id)

        return custom_sofa

    def get_next_id(self):

        dao = CustomSofa_dao()

        next_id = dao.get_next_id()

        return next_id