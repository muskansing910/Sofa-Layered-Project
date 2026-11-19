from dao.back_design_dao import BackDesign_dao


class BackDesign_service:

    def add_back_design(self, back_design):

        dao = BackDesign_dao()

        dao.add_back_design(back_design)


    def display_back_designs(self):

        dao = BackDesign_dao()

        back_designs = dao.display_all()

        return back_designs

    def display_active_back_designs(self):

        dao = BackDesign_dao()

        back_designs = dao.display_active_back_designs()

        return back_designs