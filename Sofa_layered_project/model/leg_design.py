class LegDesign:

    def __init__(self, leg_design_id, leg_design_name,
                 material, description, image,
                 status, created_at):

        self.leg_design_id = leg_design_id
        self.leg_design_name = leg_design_name
        self.material = material
        self.description = description
        self.image = image
        self.status = status
        self.created_at = created_at