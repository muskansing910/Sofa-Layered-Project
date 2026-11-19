class Admin:

    def __init__(self, admin_id,
                 name,
                 phone,
                 email,
                 password,
                 status,
                 created_at):

        self.admin_id = admin_id
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.status = status
        self.created_at = created_at