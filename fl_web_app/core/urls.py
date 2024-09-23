from django.urls import path
from .views import (SchedaLavorazioneListView, SchedaLavorazioneDetailView
                    )

app_name="core"

urlpatterns = [
    
    # Home Core
    path('', SchedaLavorazioneListView.as_view(), name='scheda_lavorazione_listview'),  
    path('scheda/<int:pk>/', SchedaLavorazioneDetailView.as_view(), name='scheda_detail'),  

    
    
]