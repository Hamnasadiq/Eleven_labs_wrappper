import requests

class ElevenLabsClient:
    BASE_URL = "https://api.elevenlabs.io/v1/convai/agents"

    def __init__(self, api_key):
        self.headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }

    def create_agent(self, config_data):
        return requests.post(f"{self.BASE_URL}/create", headers=self.headers, json=config_data)

    def get_agent(self, agent_id):
        return requests.get(f"{self.BASE_URL}/{agent_id}", headers=self.headers)

    def list_agents(self):
        return requests.get(self.BASE_URL, headers=self.headers)

    def update_agent(self, agent_id, update_data):
        return requests.patch(f"{self.BASE_URL}/{agent_id}", headers=self.headers, json=update_data)

    def delete_agent(self, agent_id):
        return requests.delete(f"{self.BASE_URL}/{agent_id}", headers=self.headers)

    def duplicate_agent(self, agent_id):
        return requests.post(f"{self.BASE_URL}/{agent_id}/duplicate", headers=self.headers)

    def get_link(self, agent_id):
        return requests.get(f"{self.BASE_URL}/{agent_id}/link", headers=self.headers)
