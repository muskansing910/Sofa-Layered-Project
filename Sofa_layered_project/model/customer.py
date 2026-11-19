class Customer:

    def __init__(self, customer_id, name, phone, email,
                 password_hash, address, city, created_at):

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.password_hash = password_hash
        self.address = address
        self.city = city
        self.created_at = created_at