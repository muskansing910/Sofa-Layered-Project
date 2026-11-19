class CustomSofa:

    def __init__(self, custom_sofa_id,
                 customer_id,
                 sofa_type_id,
                 design_id,
                 fabric_id,
                 color_id,
                 back_design_id,
                 armrest_design_id,
                 leg_design_id,
                 foam_type_id,
                 length,
                 width,
                 height,
                 seat_depth,
                 number_of_seats,
                 custom_requirements,
                 created_at):

        self.custom_sofa_id = custom_sofa_id
        self.customer_id = customer_id
        self.sofa_type_id = sofa_type_id
        self.design_id = design_id
        self.fabric_id = fabric_id
        self.color_id = color_id
        self.back_design_id = back_design_id
        self.armrest_design_id = armrest_design_id
        self.leg_design_id = leg_design_id
        self.foam_type_id = foam_type_id
        self.length = length
        self.width = width
        self.height = height
        self.seat_depth = seat_depth
        self.number_of_seats = number_of_seats
        self.custom_requirements = custom_requirements
        self.created_at = created_at