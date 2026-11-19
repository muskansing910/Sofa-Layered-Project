from dao.sofa_design_dao import SofaDesign_dao


class SofaDesignService:

    def __init__(self):

        self.sofa_design_dao = SofaDesign_dao()

    def display_active_designs(self):

        designs = self.sofa_design_dao.display_active_designs()

        return designs