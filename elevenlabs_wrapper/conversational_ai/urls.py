from django.urls import path
from .views import CreateAgentView, AgentDetailView, AgentUtilityView,CreateConversationView, ListConversationsView,ConversationDetailView
# from .views import ConversationAudioView,SignedAudioURLView,ConversationFeedbackView,CreateConversationView, ConversationDetailView,SendUserInputView

urlpatterns = [
    path('agents/create/', CreateAgentView.as_view(), name='create-agent'),
    path('agents/<str:agent_id>/', AgentDetailView.as_view(), name='agent-detail'),
    path('agents/<str:agent_id>/duplicate/', AgentUtilityView.as_view(), name='duplicate-agent'),
    path('agents/<str:agent_id>/link/', AgentUtilityView.as_view(), name='agent-link'),
    path('agents/', AgentUtilityView.as_view(), name='list-agents'),
 
#   list conversation
    path('conversations/list/', ListConversationsView.as_view(), name='list-conversations'),
    # get detail conversation
    path('conversations/<str:conversation_id>/', ConversationDetailView.as_view(), name='conversation-detail'),
    #create conversation
    path('conversations/', CreateConversationView.as_view(), name='create-conversation'),

    # path('conversations/', CreateConversationView.as_view(), name='create-conversation'),
    # path('conversations/<str:conversation_id>/input/', SendUserInputView.as_view(), name='send-user-input'),
    # path('conversations/<str:conversation_id>/audio/', ConversationAudioView.as_view(), name='conversation-audio'),
    # path('conversations/<str:conversation_id>/audio/signed-url/', SignedAudioURLView.as_view(), name='signed-audio-url'),
    # path('conversations/<str:conversation_id>/feedback/', ConversationFeedbackView.as_view(), name='conversation-feedback'),

]


