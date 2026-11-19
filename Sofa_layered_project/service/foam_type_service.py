from dao.foam_type_dao import FoamType_dao


class FoamType_service:

    def add_foam_type(self, foam_type):

        dao = FoamType_dao()

        dao.add_foam_type(foam_type)


    def display_foam_types(self):

        dao = FoamType_dao()

        foam_types = dao.display_all()

        return foam_types
    def display_active_foam_types(self):

        dao = FoamType_dao()

        foam_types = dao.display_active_foam_types()

        return foam_types

