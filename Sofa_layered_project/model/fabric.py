class Fabric:

    def __init__(self, fabric_id, fabric_name,
                 description, price_per_meter,
                 image, status, created_at):

        self.fabric_id = fabric_id
        self.fabric_name = fabric_name
        self.description = description
        self.price_per_meter = price_per_meter
        self.image = image
        self.status = status
        self.created_at = created_at