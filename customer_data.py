import json

class Customer:
    def __init__(self, customer_id, name, email, age, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.email}, {self.age}, {self.address})"

    def update_email(self, new_email):
        self.email = new_email

    @classmethod
    def load_customers_from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            customers = [cls(**item) for item in data]
            return customers

json_file_path = 'customers.json'


customers = Customer.load_customers_from_json(json_file_path)


for customer in customers:
    print(customer)


customers[0].update_email('newemail@example.com')
print(customers[0])
