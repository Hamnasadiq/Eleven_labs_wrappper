from django.views import View
from django.http import JsonResponse
from django.conf import settings
from .elevenlabs_client import ElevenLabsClient
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import uuid



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

    def post(self, request, agent_id=None):
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

#--------agents view------------




@method_decorator(csrf_exempt, name='dispatch')
class ListConversationsView(View):
    def get(self, request):
        try:
            response = client.list_conversations()
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ConversationDetailView(View):
    def get(self, request, conversation_id):
        try:
            response = client.get_conversation(conversation_id)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
@method_decorator(csrf_exempt, name='dispatch')
class CreateConversationView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            agent_id = data.get("agent_id")

            if not agent_id:
                return JsonResponse({"error": "agent_id is required"}, status=400)

            payload = {
                "agent_id": agent_id,
                "name": "Hamna's Test Conversation"
            }

            response = client.create_conversation(payload)

            try:
                return JsonResponse(response.json(), status=response.status_code)
            except json.JSONDecodeError:
                return JsonResponse({"error": response.text}, status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)




# @method_decorator(csrf_exempt, name='dispatch')
# class SendUserInputView(View):
#     def post(self, request, conversation_id):
#         try:
#             data = json.loads(request.body)
#             print(f"📨 Sending to conversation: {conversation_id} with data: {data}")
#             response = client.send_user_input(conversation_id, data)
#             return JsonResponse(response.json(), status=response.status_code)
#         except Exception as e:
#             print("❌ Error sending user input:", e)
#             return JsonResponse({"error": str(e)}, status=500)

# @method_decorator(csrf_exempt, name='dispatch')
# class ConversationAudioView(View):
#     def get(self, request, conversation_id):
#         try:
#             response = client.get_conversation_audio(conversation_id)
#             return HttpResponse(response.content, content_type='audio/mpeg', status=response.status_code)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)


# @method_decorator(csrf_exempt, name='dispatch')
# class SignedAudioURLView(View):
#     def get(self, request, conversation_id):
#         try:
#             response = client.get_signed_audio_url(conversation_id)
#             return JsonResponse(response.json(), status=response.status_code)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)


# @method_decorator(csrf_exempt, name='dispatch')
# class ConversationFeedbackView(View):
#     def post(self, request, conversation_id):
#         try:
#             data = json.loads(request.body)
#             response = client.send_conversation_feedback(conversation_id, data)
#             return JsonResponse(response.json(), status=response.status_code)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)





