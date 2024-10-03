from django import forms
from .models import SchedaLavorazione

class SchedaLavorazioneNoteForm(forms.ModelForm):
    class Meta:
        model = SchedaLavorazione
        fields = ['note_da_macchina']
        widgets = {
            'note_da_macchina': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'note_da_macchina': 'Note da Macchina'
        }
