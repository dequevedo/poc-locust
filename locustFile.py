from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def create_product(self):
        payload = {
            "name": "Sobremesa teste",
            "price": 5.0,
            "description": "Teste decription",
            "category": "SOBREMESA"
        }
        headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }
        self.client.post("/v1/products", json=payload, headers=headers)
