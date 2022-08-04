from locust import HttpUser, task, between
import json


class loadtest_get_api(HttpUser):
    wait_time = between(1, 5)
    username = 'admin'
    password = 'secret'
    campaign_url = "/campaign/events/?campaign_id=5003"

    @task
    def test_campaign(self):
        self.client.get(self.campaign_url)

    def on_start(self):
        auth = self.client.post("/token", data={"username": self.username, "password": self.password})
        auth = json.loads(auth.text)
        self.client.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + auth["access_token"]
        }