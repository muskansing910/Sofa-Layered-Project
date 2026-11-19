from dao.leg_design_dao import LegDesign_dao


class LegDesign_service:

    def add_leg_design(self, leg_design):

        dao = LegDesign_dao()

        dao.add_leg_design(leg_design)


    def display_leg_designs(self):

        dao = LegDesign_dao()

        leg_designs = dao.display_all()

        return leg_designs
    def display_active_leg_designs(self):

        dao = LegDesign_dao()

        leg_designs = dao.display_active_leg_designs()

        return leg_designs