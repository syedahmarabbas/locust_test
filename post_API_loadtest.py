from locust import HttpUser, task, between
import random
import json


class loadtest_post_api(HttpUser):
    wait_time = between(1, 5)
    connection_timeout = 120.0
    network_timeout = 120.0


    @task
    def test_event(self):
        session_ids = ['Session1', 'Session2', 'Session3', 'Session4', 'Session5', 'Session6', 'Session7', 'Session8']
        events = ['lead_submission', 'page_view', 'open_form']

        self.client.post("/event", json={
            "session": {
                "user_agent": "string",
                "ip_address": "string",
                "cookie": "string",
                "session_id": random.choice(session_ids),
                "user_id": "string",
                "tracking_parameters": {
                    "campaign": "70b4ab86-1f7d-42be-b73e-5df9f81871e4",
                    "source": "google"
                },
                "fb_click_id": "string",
                "fb_browser_id": "string",
                "google_click_id": "string",
                "display_click_id": "string"
            },
            "url": "https://www.analyticsloadtest.com",
            "event_time": "2022-08-03T15:27:03.647Z",
            "event_type": random.choice(events),
            "project_id": "cca7e99a-5633-4d12-980a-a26be8bc508d",
            "unit_id": "string"
        })
