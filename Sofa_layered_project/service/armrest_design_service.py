from dao.armrest_design_dao import ArmrestDesign_dao


class ArmrestDesign_service:

    def add_armrest_design(self, armrest_design):

        dao = ArmrestDesign_dao()

        dao.add_armrest_design(armrest_design)


    def display_armrest_designs(self):

        dao = ArmrestDesign_dao()

        armrest_designs = dao.display_all()

        return armrest_designs

    def display_active_armrest_designs(self):

        dao = ArmrestDesign_dao()

        armrest_designs = dao.display_active_armrest_designs()

        return armrest_designs