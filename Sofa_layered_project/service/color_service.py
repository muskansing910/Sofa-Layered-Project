from dao.color_dao import Color_dao


class Color_service:

    def add_color(self, color):

        dao = Color_dao()

        dao.add_color(color)


    def display_colors(self):

        dao = Color_dao()

        colors = dao.display_all()

        return colors

    def display_active_colors(self):

        dao = Color_dao()

        colors = dao.display_active_colors()

        return colors