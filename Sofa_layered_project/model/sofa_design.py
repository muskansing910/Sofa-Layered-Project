class SofaDesign:

    def __init__(self, design_id, sofa_type_id,
                 design_name, description,
                 starting_price, image,
                 status, created_at):

        self.design_id = design_id
        self.sofa_type_id = sofa_type_id
        self.design_name = design_name
        self.description = description
        self.starting_price = starting_price
        self.image = image
        self.status = status
        self.created_at = created_at