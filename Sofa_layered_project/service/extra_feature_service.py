from dao.extra_feature_dao import ExtraFeature_dao


class ExtraFeature_service:

    def add_extra_feature(self, extra_feature):

        dao = ExtraFeature_dao()

        dao.add_extra_feature(extra_feature)


    def display_extra_features(self):

        dao = ExtraFeature_dao()

        extra_features = dao.display_all()

        return extra_features