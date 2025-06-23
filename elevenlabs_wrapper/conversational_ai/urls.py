from django.urls import path
from .views import CreateAgentView, AgentDetailView, AgentUtilityView

urlpatterns = [
    path('agents/create/', CreateAgentView.as_view(), name='create-agent'),
    path('agents/<str:agent_id>/', AgentDetailView.as_view(), name='agent-detail'),
    path('agents/<str:agent_id>/duplicate/', AgentUtilityView.as_view(), name='duplicate-agent'),
    path('agents/<str:agent_id>/link/', AgentUtilityView.as_view(), name='agent-link'),
    path('agents/', AgentUtilityView.as_view(), name='list-agents'),
]
