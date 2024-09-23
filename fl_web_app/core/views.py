from django.shortcuts import render
import barcode
from io import BytesIO
import base64
from barcode.writer import ImageWriter
from django.views.generic import ListView, DetailView
from .models import SchedaLavorazione  # Importa il modello


class SchedaLavorazioneListView(ListView):
    model = SchedaLavorazione  # Modello da visualizzare
    template_name = 'core/scheda_lavorazione_list.html'  # Template da usare
    context_object_name = 'schede'  # Nome con cui accedere ai dati nel template

    # Se vuoi ordinare i risultati, puoi aggiungere il seguente attributo:
    ordering = ['-created_at']  # Ordina per data di creazione, decrescente
    
class SchedaLavorazioneDetailView(DetailView):
    model = SchedaLavorazione
    template_name = 'core/scheda_detail.html'  # Assicurati di avere un template per il dettaglio
    context_object_name = 'scheda'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scheda = self.get_object()
        barcode_value = f"{scheda.id_scheda}{scheda.created_at.strftime('%Y%m%d')}"
        print(f"barcode_value: {barcode_value}")
        # Prova a ottenere la classe del codice a barre
        barcode_class = barcode.get_barcode_class('code128')
        if barcode_class is None:
            raise ValueError("Errore nel recupero della classe barcode per code128")

        # Genera il codice a barre
        barcode_obj = barcode_class(barcode_value, writer=ImageWriter())
        if barcode_obj is None:
            raise ValueError("Errore nel recupero della classe barcode per oggetto")

        # Salva il codice a barre in memoria
        buffer = BytesIO()
        barcode_obj.write(buffer)

        # Converti l'immagine in base64
        barcode_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Aggiungi il codice a barre al contesto
        context['barcode_image'] = barcode_image
        return context
