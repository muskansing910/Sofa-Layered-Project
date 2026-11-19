from dao.fabric_dao import Fabric_dao


class Fabric_service:

    def add_fabric(self, fabric):

        dao = Fabric_dao()

        dao.add_fabric(fabric)


    def display_fabrics(self):

        dao = Fabric_dao()

        fabrics = dao.display_all()

        return fabrics

    def display_active_fabrics(self):

        dao = Fabric_dao()

        fabrics = dao.display_active_fabrics()

        return fabrics