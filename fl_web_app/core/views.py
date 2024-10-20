from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import barcode
from io import BytesIO
import base64
from barcode.writer import ImageWriter
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .forms import SchedaLavorazioneNoteForm

from .models import SchedaLavorazione  # Importa il modello

from django.http import JsonResponse
from django.core.paginator import Paginator



def get_data(request):
    try:
        page_number = request.GET.get('page', 1)  # Ottieni il numero di pagina dalla richiesta
        schede = SchedaLavorazione.objects.select_related('idcliente', 'idgruppo').values(
            'id_scheda',
            'created_at',
            'idcliente__ragionesociale',  # Assicurati che questo campo esista nel modello Cliente
            'idgruppo__descrizione'  # Assicurati che questo campo esista nel modello Gruppo
        ).order_by('-id_scheda')  # Ordina i dati per id_scheda

        paginator = Paginator(schede, 10)  # Mostra 10 schede per pagina
        page_obj = paginator.get_page(page_number)

        return JsonResponse({
            'dati': list(page_obj),  # Restituisci i dati della pagina corrente
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'current_page': page_obj.number,
            'total_pages': paginator.num_pages
        }, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class SchedaLavorazioneListView(ListView):
    model = SchedaLavorazione  # Modello da visualizzare
    template_name = 'core/scheda_lavorazione_list.html'  # Template da usare
    context_object_name = 'schede'  # Nome con cui accedere ai dati nel template

    # Se vuoi ordinare i risultati, puoi aggiungere il seguente attributo:
    ordering = ['-created_at']  # Ordina per data di creazione, decrescente
    paginate_by = 10  # Numero di record per pagina
    
class SchedaLavorazioneDetailView(DetailView):
    model = SchedaLavorazione
    template_name = 'core/scheda_detail.html'  # Assicurati di avere un template per il dettaglio
    context_object_name = 'scheda'
    form_class = SchedaLavorazioneNoteForm
    
    def get_success_url(self):
        return reverse_lazy('core:scheda_detail', kwargs={'pk': self.object.pk})
    
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
        context['form'] = SchedaLavorazioneNoteForm(instance=self.object) 
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance = self.get_object()
        form.save()
        return super().form_valid(form)
    

class SchedaLavorazioneUpdateView(UpdateView):
    model = SchedaLavorazione
    form_class = SchedaLavorazioneNoteForm
    template_name = 'core/scheda_detail.html'
    context_object_name = 'scheda'
    success_message = ' - Nota modificata correttamente!'
    

    def get_success_url(self):
        # Redirect alla pagina di dettaglio della scheda
        return reverse_lazy('core:scheda_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.info(self.request, self.success_message)
        return super().form_valid(form)

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