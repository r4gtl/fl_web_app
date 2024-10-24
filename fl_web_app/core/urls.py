from django.urls import path
from .views import (SchedaLavorazioneListView, SchedaLavorazioneDetailView, SchedaLavorazioneUpdateView,
                    get_data,
                    )

app_name="core"

urlpatterns = [
    
    # Home Core
    path('', SchedaLavorazioneListView.as_view(), name='scheda_lavorazione_listview'),  
    # path('scheda/<int:pk>/', SchedaLavorazioneDetailView.as_view(), name='scheda_detail'),  
    path('scheda/<int:pk>/', SchedaLavorazioneUpdateView.as_view(), name='scheda_detail'), 
    path('get-data/', get_data, name='get_data'),
    

    
    
]