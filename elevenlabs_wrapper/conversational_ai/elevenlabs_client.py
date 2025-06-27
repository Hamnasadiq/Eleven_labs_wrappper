import requests

class ElevenLabsClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"

    def _headers(self):
        return {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    # ----------------- AGENTS -----------------
    def create_agent(self, data):
        return requests.post(f"{self.base_url}/convai/agents/create", headers=self._headers(), json=data)

    def get_agent(self, agent_id):
        return requests.get(f"{self.base_url}/convai/agents/{agent_id}", headers=self._headers())

    def update_agent(self, agent_id, data):
        return requests.patch(f"{self.base_url}/convai/agents/{agent_id}", headers=self._headers(), json=data)

    def delete_agent(self, agent_id):
        return requests.delete(f"{self.base_url}/convai/agents/{agent_id}", headers=self._headers())

    def list_agents(self):
        return requests.get(f"{self.base_url}/convai/agents", headers=self._headers())

    def duplicate_agent(self, agent_id):
        return requests.post(f"{self.base_url}/convai/agents/{agent_id}/duplicate", headers=self._headers())

    def get_link(self, agent_id):
        return requests.get(f"{self.base_url}/convai/agents/{agent_id}/link", headers=self._headers())

    # ----------------- CONVERSATIONS -----------------
    
    
    def list_conversations(self):
         return requests.get(f"{self.base_url}/convai/conversations", headers=self._headers())


    def get_conversation(self, conversation_id):
        url = f"{self.base_url}/convai/conversations/{conversation_id}"
        return requests.get(url, headers=self.headers)    

   
    def create_conversation(self, data):
        url = f"{self.base_url}/convai/conversations"
        print("📡 Sending request to:", url)
        print("📦 Payload:", data)

        response = requests.post(url, headers=self._headers(), json=data)

        print("📬 Response status:", response.status_code)
        print("📬 Response content:", response.text)

        return response

















    # def create_conversation(self, data):
    #     print("📡 Creating conversation with:", data)
    #     response = requests.post(f"{self.base_url}/conversations", headers=self._headers(), json=data)
    #     print("📥 Response:", response.status_code, response.text)
    #     return response



    

    # def delete_conversation(self, conversation_id):
    #     return requests.delete(f"{self.base_url}/conversations/{conversation_id}", headers=self._headers())
    

    # def get_conversation_audio(self, conversation_id):
    #     return requests.get(f"{self.base_url}/conversations/{conversation_id}/audio", headers=self._headers())

    # def get_signed_audio_url(self, conversation_id):
    #     return requests.get(f"{self.base_url}/conversations/{conversation_id}/audio/signed-url", headers=self._headers())

    # def send_conversation_feedback(self, conversation_id, data):
    #     return requests.post(f"{self.base_url}/conversations/{conversation_id}/feedback", headers=self._headers(), json=data)
    # def send_user_input(self, conversation_id, data):
    #     url = f"https://api.elevenlabs.io/conversations/{conversation_id}/input"
    #     return requests.post(url, headers=self._headers(), json=data)
