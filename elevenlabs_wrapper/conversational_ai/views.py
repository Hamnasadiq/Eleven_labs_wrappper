from django.views import View
from django.http import JsonResponse
from django.conf import settings
from .elevenlabs_client import ElevenLabsClient
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

s
API_KEY = settings.ELEVENLABS_API_KEY


client = ElevenLabsClient(api_key=API_KEY)



@method_decorator(csrf_exempt, name='dispatch')
class CreateAgentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            response = client.create_agent(data)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class AgentDetailView(View):
    def get(self, request, agent_id):
        try:
            response = client.get_agent(agent_id)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def patch(self, request, agent_id):
        try:
            data = json.loads(request.body)
            response = client.update_agent(agent_id, data)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def delete(self, request, agent_id):
        try:
            response = client.delete_agent(agent_id)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class AgentUtilityView(View):
    def get(self, request):
        try:
            response = client.list_agents()
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def post(self, request, agent_id):
        try:
            if "duplicate" in request.path:
                response = client.duplicate_agent(agent_id)
            elif "link" in request.path:
                response = client.get_link(agent_id)
            else:
                return JsonResponse({"error": "Invalid action"}, status=400)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
