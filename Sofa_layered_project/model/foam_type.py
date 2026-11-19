class FoamType:

    def __init__(self, foam_type_id, foam_type_name,
                 density, description,
                 price_per_cubic_ft, status, created_at):

        self.foam_type_id = foam_type_id
        self.foam_type_name = foam_type_name
        self.density = density
        self.description = description
        self.price_per_cubic_ft = price_per_cubic_ft
        self.status = status
        self.created_at = created_at