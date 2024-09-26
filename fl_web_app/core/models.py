# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TFormatocolonne(models.Model):
    nomemaschera = models.CharField(db_column='NomeMaschera', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomesottomaschera = models.CharField(db_column='NomeSottoMaschera', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomecolonna = models.CharField(db_column='NomeColonna', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ordinecolonna = models.IntegerField(db_column='OrdineColonna', blank=True, null=True)  # Field name made lowercase.
    larghezzacolonna = models.IntegerField(db_column='LarghezzaColonna', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_FormatoColonne'


class TRicerca(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chiave = models.CharField(db_column='Chiave', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipochiavetesto = models.BooleanField(db_column='TipoChiaveTesto', blank=True, null=True)  # Field name made lowercase.
    strsql = models.TextField(db_column='strSQL', blank=True, null=True)  # Field name made lowercase.
    ordinamento = models.CharField(db_column='Ordinamento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ordinamento2 = models.CharField(db_column='Ordinamento2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campi = models.CharField(db_column='Campi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colonne = models.IntegerField(db_column='Colonne', blank=True, null=True)  # Field name made lowercase.
    larghezza = models.CharField(db_column='Larghezza', max_length=100, blank=True, null=True)  # Field name made lowercase.
    predefinito = models.CharField(db_column='Predefinito', max_length=50, blank=True, null=True)  # Field name made lowercase.
    originecombo = models.CharField(db_column='OrigineCombo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dacompilare = models.CharField(db_column='DaCompilare', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vaiarecord = models.BooleanField(db_column='VaiaRecord', blank=True, null=True)  # Field name made lowercase.
    formriferimento = models.CharField(db_column='FormRiferimento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mionome = models.CharField(db_column='MioNome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    focus = models.CharField(db_column='Focus', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_Ricerca'


class Utenti(models.Model):
    idutente = models.AutoField(db_column='IDUtente', primary_key=True)  # Field name made lowercase.
    nomecomputer = models.CharField(db_column='NomeComputer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    utente = models.CharField(db_column='Utente', max_length=50, blank=True, null=True)  # Field name made lowercase.
    percorsotabelle = models.CharField(db_column='PercorsoTabelle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    percorsifilebackup = models.CharField(db_column='PercorsiFileBackup', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Utenti'


class DettaglioSkPressa(models.Model):
    id_dettaglio_sk_pressa = models.AutoField(primary_key=True)
    id_scheda = models.ForeignKey('SchedaLavorazione', on_delete=models.CASCADE, blank=True, null=True)
    programma_pressa = models.CharField(max_length=255, blank=True, null=True)
    riservato = models.CharField(max_length=255, blank=True, null=True)
    pressione_stiratura = models.IntegerField(blank=True, null=True)
    tempo_stiratura = models.IntegerField(blank=True, null=True)
    pressione_placcatura = models.IntegerField(blank=True, null=True)
    doppia_stiratura_pressione1 = models.IntegerField(blank=True, null=True)
    doppia_stiratura_pressione2 = models.IntegerField(blank=True, null=True)
    doppia_stiratura_tempo1 = models.IntegerField(blank=True, null=True)
    doppia_stiratura_tempo2 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_pressione1 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_pressione2 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_pressione3 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_tempo1 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_tempo2 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_tempo3 = models.IntegerField(blank=True, null=True)
    battute_multiple_pressione_chiusura = models.IntegerField(blank=True, null=True)
    battute_multiple_pressione_inferiore = models.IntegerField(blank=True, null=True)
    battute_multiple_pressione_successive = models.IntegerField(blank=True, null=True)
    tempo_chiusura_battute_multiple = models.IntegerField(blank=True, null=True)
    tempi_successivi_battute_multiple = models.IntegerField(blank=True, null=True)
    numero_chiusure_battute_multiple = models.IntegerField(blank=True, null=True)
    temperatura1 = models.IntegerField(blank=True, null=True)
    temperatura2 = models.IntegerField(blank=True, null=True)
    temperatura3 = models.IntegerField(blank=True, null=True)
    temperatura4 = models.IntegerField(blank=True, null=True)
    temperatura5 = models.IntegerField(blank=True, null=True)
    temperatura6 = models.IntegerField(blank=True, null=True)
    temperatura7 = models.IntegerField(blank=True, null=True)
    temperatura8 = models.IntegerField(blank=True, null=True)
    temperatura9 = models.IntegerField(blank=True, null=True)
    temperatura10 = models.IntegerField(blank=True, null=True)
    temperatura11 = models.IntegerField(blank=True, null=True)
    temperatura12 = models.IntegerField(blank=True, null=True)
    temperatura13 = models.IntegerField(blank=True, null=True)
    temperatura14 = models.IntegerField(blank=True, null=True)
    temperatura15 = models.IntegerField(blank=True, null=True)
    temperatura16 = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    idmateriale = models.ForeignKey('Tblmateriali', models.DO_NOTHING, db_column='idmateriale', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dettaglio_sk_pressa'


class ImpostazionePressa(models.Model):
    id_impostazione = models.AutoField(primary_key=True)
    id_ricetta = models.ForeignKey('Ricetta', on_delete=models.CASCADE, blank=True, null=True)
    programma_pressa = models.CharField(max_length=255, blank=True, null=True)
    riservato = models.CharField(max_length=255, blank=True, null=True)
    pressione_stiratura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tempo_stiratura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pressione_placcatura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    doppia_stiratura_pressione1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    doppia_stiratura_pressione2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    doppia_stiratura_tempo1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    doppia_stiratura_tempo2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tripla_stiratura_pressione1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tripla_stiratura_pressione2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tripla_stiratura_pressione3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tripla_stiratura_tempo1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tripla_stiratura_tempo2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tripla_stiratura_tempo3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    battute_multiple_pressione_chiusura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    battute_multiple_pressione_inferiore = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    battute_multiple_pressione_successive = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tempo_chiusura_battute_multiple = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tempi_successivi_battute_multiple = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    numero_chiusure_battute_multiple = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura5 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura6 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura7 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura8 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura9 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura10 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura11 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura12 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura13 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura14 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura15 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    temperatura16 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    idmateriale = models.ForeignKey('Tblmateriali', models.DO_NOTHING, db_column='idmateriale', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impostazione_pressa'


class ProgrammaPressa(models.Model):
    id_programma_pressa = models.AutoField(primary_key=True)
    descrizione = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programma_pressa'
        
    def __str__(self):
        return self.descrizione


class Ricetta(models.Model):
    id_ricetta = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey('TblClienti', on_delete=models.CASCADE, blank=True, null=True)
    idgruppo = models.ForeignKey('Tblgruppi', on_delete=models.CASCADE ,blank=True, null=True)
    idcolore = models.ForeignKey('TblColori', on_delete=models.CASCADE ,blank=True, null=True)
    idtipostampa = models.ForeignKey('Tbltipistampe', on_delete=models.CASCADE, blank=True, null=True)
    idfase = models.ForeignKey('Tblfasi', on_delete=models.CASCADE, blank=True, null=True)
    idmacchinario = models.ForeignKey('Tblmacchine', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ricetta'



class RiscontroPressa(models.Model):
    id_riscontro = models.AutoField(primary_key=True)
    id_scheda = models.IntegerField(blank=True, null=True)
    data_inizio = models.DateTimeField(blank=True, null=True)
    ora_inizio = models.DateTimeField(blank=True, null=True)
    data_fine = models.DateTimeField(blank=True, null=True)
    ora_fine = models.DateTimeField(blank=True, null=True)
    numero_pelli = models.IntegerField(blank=True, null=True)
    programma_pressa = models.CharField(max_length=255, blank=True, null=True)
    pressione_stiratura = models.IntegerField(blank=True, null=True)
    tempo_stiratura = models.IntegerField(blank=True, null=True)
    pressione_placcatura = models.IntegerField(blank=True, null=True)
    doppia_stiratura_pressione1 = models.IntegerField(blank=True, null=True)
    doppia_stiratura_pressione2 = models.IntegerField(blank=True, null=True)
    doppia_stiratura_tempo1 = models.IntegerField(blank=True, null=True)
    doppia_stiratura_tempo2 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_pressione1 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_pressione2 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_pressione3 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_tempo1 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_tempo2 = models.IntegerField(blank=True, null=True)
    tripla_stiratura_tempo3 = models.IntegerField(blank=True, null=True)
    battute_multiple_pressione_chiusura = models.IntegerField(blank=True, null=True)
    battute_multiple_pressione_inferiore = models.IntegerField(blank=True, null=True)
    battute_multiple_pressione_successive = models.IntegerField(blank=True, null=True)
    tempo_chiusura_battute_multiple = models.IntegerField(blank=True, null=True)
    tempi_successivi_battute_multiple = models.IntegerField(blank=True, null=True)
    numero_chiusure_battute_multiple = models.IntegerField(blank=True, null=True)
    temperatura1 = models.IntegerField(blank=True, null=True)
    temperatura2 = models.IntegerField(blank=True, null=True)
    temperatura3 = models.IntegerField(blank=True, null=True)
    tempant = models.IntegerField(blank=True, null=True)
    temppost = models.IntegerField(blank=True, null=True)
    temperatura4 = models.IntegerField(blank=True, null=True)
    temperatura5 = models.IntegerField(blank=True, null=True)
    temperatura6 = models.IntegerField(blank=True, null=True)
    temperatura7 = models.IntegerField(blank=True, null=True)
    temperatura8 = models.IntegerField(blank=True, null=True)
    temperatura9 = models.IntegerField(blank=True, null=True)
    temperatura10 = models.IntegerField(blank=True, null=True)
    temperatura11 = models.IntegerField(blank=True, null=True)
    temperatura12 = models.IntegerField(blank=True, null=True)
    temperatura13 = models.IntegerField(blank=True, null=True)
    temperatura14 = models.IntegerField(blank=True, null=True)
    temperatura15 = models.IntegerField(blank=True, null=True)
    temperatura16 = models.IntegerField(blank=True, null=True)
    tensione_fase1 = models.IntegerField(blank=True, null=True)
    tensione_fase2 = models.IntegerField(blank=True, null=True)
    tensione_fase3 = models.IntegerField(blank=True, null=True)
    corrente_fase1 = models.IntegerField(blank=True, null=True)
    corrente_fase2 = models.IntegerField(blank=True, null=True)
    corrente_fase3 = models.IntegerField(blank=True, null=True)
    potenza_attiva = models.IntegerField(blank=True, null=True)
    potenza_reattiva = models.IntegerField(blank=True, null=True)
    contatore_energia_attiva = models.IntegerField(blank=True, null=True)
    contatore_energia_reattiva = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riscontro_pressa'


class SchedaLavorazione(models.Model):
    id_scheda = models.AutoField(primary_key=True)
    id_ricetta = models.ForeignKey('Ricetta', on_delete=models.CASCADE, blank=True, null=True, db_column='id_ricetta')
    idcliente = models.ForeignKey('TblClienti', on_delete=models.CASCADE, blank=True, null=True, db_column='idcliente')
    idgruppo = models.ForeignKey('Tblgruppi', on_delete=models.CASCADE ,blank=True, null=True, db_column='idgruppo')
    idcolore = models.ForeignKey('TblColori', on_delete=models.CASCADE ,blank=True, null=True, db_column='idcolore')
    idtipostampa = models.ForeignKey('Tbltipistampe', on_delete=models.CASCADE, blank=True, null=True, db_column='idtipostampa')
    idfase = models.ForeignKey('Tblfasi', on_delete=models.CASCADE, blank=True, null=True, db_column='idfase')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    rif_ddt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheda_lavorazione'
    
    def __str__(self):
        return (f"Scheda N. {self.id_scheda} del {self.created_at}")


class Tblazienda(models.Model):
    idragsoc = models.AutoField(db_column='IDRagSoc', primary_key=True)  # Field name made lowercase.
    ragionesociale = models.CharField(db_column='RagioneSociale', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indirizzo = models.CharField(db_column='Indirizzo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cap = models.CharField(db_column='CAP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comune = models.CharField(db_column='Comune', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    partitaiva = models.CharField(db_column='PartitaIVA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ufficio = models.CharField(db_column='Ufficio', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAzienda'


class Tblclienti(models.Model):
    idcliente = models.AutoField(db_column='IDCliente', primary_key=True)  # Field name made lowercase.
    ragionesociale = models.CharField(db_column='RagioneSociale', max_length=100, blank=True, null=True)  # Field name made lowercase.
    indirizzo = models.CharField(db_column='Indirizzo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cap = models.CharField(db_column='CAP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    città = models.CharField(db_column='Città', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    piva = models.CharField(db_column='PIVA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cf = models.CharField(db_column='CF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ufficioiva = models.CharField(db_column='UfficioIVA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idpagamento = models.IntegerField(db_column='IDPagamento', blank=True, null=True)  # Field name made lowercase.
    idiva = models.IntegerField(db_column='IDIVA', blank=True, null=True)  # Field name made lowercase.
    idbanca = models.IntegerField(db_column='IDBanca', blank=True, null=True)  # Field name made lowercase.
    agenzia = models.CharField(db_column='Agenzia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iban = models.CharField(db_column='IBAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nascondi = models.BooleanField(db_column='Nascondi', blank=True, null=True)  # Field name made lowercase.
    idum = models.IntegerField(db_column='IDUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblClienti'
    
    def __str__(self):
        return self.ragionesociale


class Tblcolori(models.Model):
    idcolore = models.AutoField(db_column='IDColore', primary_key=True)  # Field name made lowercase.
    colore = models.CharField(db_column='Colore', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblColori'
    
    def __str__(self):
        return self.colore


class Tblddtingresso(models.Model):
    idddtingresso = models.AutoField(db_column='IDDDTIngresso', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('TblClienti', on_delete=models.CASCADE, blank=True, null=True)
    numero = models.CharField(db_column='Numero', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    noteindettaglio = models.BooleanField(db_column='NoteInDettaglio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDDTIngresso'


class Tblddtuscita(models.Model):
    idddtuscita = models.AutoField(db_column='IDDDTUscita', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey('TblClienti', on_delete=models.CASCADE, blank=True, null=True)
    numero = models.CharField(db_column='Numero', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDDTUscita'


class Tbldettddtingresso(models.Model):
    iddettddtingresso = models.AutoField(db_column='IDDettDDTIngresso', primary_key=True)  # Field name made lowercase.
    idddtingresso = models.IntegerField(db_column='IDDDTIngresso', blank=True, null=True)  # Field name made lowercase.
    idgruppo = models.IntegerField(db_column='IDGruppo', blank=True, null=True)  # Field name made lowercase.
    idtaglia = models.IntegerField(db_column='IDTaglia', blank=True, null=True)  # Field name made lowercase.
    idtipostampa = models.IntegerField(db_column='IDTipoStampa', blank=True, null=True)  # Field name made lowercase.
    idfase = models.IntegerField(db_column='IDFase', blank=True, null=True)  # Field name made lowercase.
    idum = models.IntegerField(db_column='IDUM', blank=True, null=True)  # Field name made lowercase.
    quantita = models.DecimalField(db_column='Quantita', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consegna = models.CharField(db_column='Consegna', max_length=255, blank=True, null=True)  # Field name made lowercase.
    evaso = models.BooleanField(db_column='Evaso', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    idcolore = models.IntegerField(db_column='IDColore', blank=True, null=True)  # Field name made lowercase.
    notedamacchina = models.TextField(db_column='NoteDaMacchina', blank=True, null=True)  # Field name made lowercase.
    idimpeff = models.IntegerField(db_column='IDImpEff', blank=True, null=True)  # Field name made lowercase.
    idimpmacchina = models.IntegerField(db_column='IDImpMacchina', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDettDDTIngresso'


class Tbldettddtuscita(models.Model):
    iddettddtuscita = models.AutoField(db_column='IDDettDDTUscita', primary_key=True)  # Field name made lowercase.
    idddtuscita = models.IntegerField(db_column='IDDDTUscita', blank=True, null=True)  # Field name made lowercase.
    idgruppo = models.IntegerField(db_column='IDGruppo', blank=True, null=True)  # Field name made lowercase.
    um = models.CharField(db_column='UM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quantita = models.DecimalField(db_column='Quantita', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDettDDTUscita'


class Tbldettmacchine(models.Model):
    iddettmacchine = models.AutoField(db_column='IDDettMacchine', primary_key=True)  # Field name made lowercase.
    idmacchina = models.IntegerField(db_column='IDMacchina', blank=True, null=True)  # Field name made lowercase.
    iddettddtingresso = models.IntegerField(db_column='IDDettDDTIngresso', blank=True, null=True)  # Field name made lowercase.
    quantita = models.DecimalField(db_column='Quantita', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datainizio = models.DateTimeField(db_column='DataInizio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblDettMacchine'


class Tblfasi(models.Model):
    idfase = models.AutoField(db_column='IDFase', primary_key=True)  # Field name made lowercase.
    fase = models.CharField(db_column='Fase', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFasi'
    
    def __str__(self):
        return self.fase



class Tblgruppi(models.Model):
    idgruppo = models.AutoField(db_column='IDGruppo', primary_key=True)  # Field name made lowercase.
    descrizione = models.CharField(db_column='Descrizione', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codice = models.CharField(db_column='Codice', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGruppi'
    
    def __str__(self):
        return self.descrizione


class Tblimpeff(models.Model):
    idimpeff = models.AutoField(db_column='IDImpEff', primary_key=True)  # Field name made lowercase.
    idddtingresso = models.IntegerField(db_column='IDDDTIngresso', blank=True, null=True)  # Field name made lowercase.
    iddettddtingresso = models.IntegerField(db_column='IDDettDDTIngresso', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='IDCliente', blank=True, null=True)  # Field name made lowercase.
    idmacchina = models.IntegerField(db_column='IDMacchina', blank=True, null=True)  # Field name made lowercase.
    idtipostampa = models.IntegerField(db_column='IDTipoStampa', blank=True, null=True)  # Field name made lowercase.
    idgruppo = models.IntegerField(db_column='IDGruppo', blank=True, null=True)  # Field name made lowercase.
    idfase = models.IntegerField(db_column='IDFase', blank=True, null=True)  # Field name made lowercase.
    pressione = models.DecimalField(db_column='Pressione', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    temperatura = models.DecimalField(db_column='Temperatura', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tempo = models.CharField(db_column='Tempo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idmateriale = models.IntegerField(db_column='IDMateriale', blank=True, null=True)  # Field name made lowercase.
    idmatinlavoro = models.IntegerField(db_column='IDMatInLavoro', blank=True, null=True)  # Field name made lowercase.
    idcolore = models.IntegerField(db_column='IDColore', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblImpEff'


class Tblimpmacchina(models.Model):
    idimpmacchina = models.AutoField(db_column='IDImpMacchina', primary_key=True)  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='IDCliente', blank=True, null=True)  # Field name made lowercase.
    idmacchina = models.IntegerField(db_column='IDMacchina', blank=True, null=True)  # Field name made lowercase.
    idtipostampa = models.IntegerField(db_column='IDTipoStampa', blank=True, null=True)  # Field name made lowercase.
    idgruppo = models.IntegerField(db_column='IDGruppo', blank=True, null=True)  # Field name made lowercase.
    idfase = models.IntegerField(db_column='IDFase', blank=True, null=True)  # Field name made lowercase.
    pressione = models.DecimalField(db_column='Pressione', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    temperatura = models.DecimalField(db_column='Temperatura', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tempo = models.CharField(db_column='Tempo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idmateriale = models.IntegerField(db_column='IDMateriale', blank=True, null=True)  # Field name made lowercase.
    idcolore = models.IntegerField(db_column='IDColore', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblImpMacchina'


class Tblmacchine(models.Model):
    idmacchina = models.AutoField(db_column='IDMacchina', primary_key=True)  # Field name made lowercase.
    descrizione = models.CharField(db_column='Descrizione', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_tipo_macchina = models.ForeignKey('TipoMacchina', on_delete=models.CASCADE, blank=True, null=True, db_column='id_tipo_macchina')

    class Meta:
        managed = False
        db_table = 'tblMacchine'
        
    def __str__(self):
        return self.descrizione


class Tblmatinlavoro(models.Model):
    idmatinlavoro = models.AutoField(db_column='IDMatInLavoro', primary_key=True)  # Field name made lowercase.
    iddettddtingresso = models.IntegerField(db_column='IDDettDDTIngresso', blank=True, null=True)  # Field name made lowercase.
    idmacchina = models.IntegerField(db_column='IDMacchina', blank=True, null=True)  # Field name made lowercase.
    quantita = models.DecimalField(db_column='Quantita', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lavorato = models.BooleanField(db_column='Lavorato', blank=True, null=True)  # Field name made lowercase.
    priorità = models.IntegerField(db_column='Priorità', blank=True, null=True)  # Field name made lowercase.
    idimpeff = models.IntegerField(db_column='IDImpEff', blank=True, null=True)  # Field name made lowercase.
    idimpmacchina = models.IntegerField(db_column='IDImpMacchina', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMatInLavoro'


class Tblmateriali(models.Model):
    idmateriale = models.AutoField(db_column='IDMateriale', primary_key=True)  # Field name made lowercase.
    materiale = models.CharField(db_column='Materiale', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMateriali'
        
    def __str__(self):
        return self.materiale


class Tblstoccaggio(models.Model):
    idstoccaggio = models.AutoField(db_column='IDStoccaggio', primary_key=True)  # Field name made lowercase.
    iddettddtingresso = models.IntegerField(db_column='IDDettDDTIngresso', blank=True, null=True)  # Field name made lowercase.
    idzonamagazzino = models.IntegerField(db_column='IDZonaMagazzino', blank=True, null=True)  # Field name made lowercase.
    quantita = models.DecimalField(db_column='Quantita', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lavorato = models.BooleanField(db_column='Lavorato', blank=True, null=True)  # Field name made lowercase.
    inlavorazione = models.BooleanField(db_column='InLavorazione', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStoccaggio'


class Tbltaglie(models.Model):
    idtaglia = models.AutoField(db_column='IDTaglia', primary_key=True)  # Field name made lowercase.
    taglia = models.CharField(db_column='Taglia', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTaglie'
        
    def __str__(self):
        return self.taglia


class Tbltipistampe(models.Model):
    idtipostampa = models.AutoField(db_column='IDTipoStampa', primary_key=True)  # Field name made lowercase.
    tipostampa = models.CharField(db_column='TipoStampa', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTipiStampe'
        
    def __str__(self):
        return self.tipostampa


class Tblum(models.Model):
    idum = models.AutoField(db_column='IDUM', primary_key=True)  # Field name made lowercase.
    um = models.CharField(db_column='UM', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUM'
        
    def __str__(self):
        return self.um


class Tblzonemagazzino(models.Model):
    idzonamagazzino = models.AutoField(db_column='IDZonaMagazzino', primary_key=True)  # Field name made lowercase.
    zonamagazzino = models.CharField(db_column='ZonaMagazzino', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblZoneMagazzino'
        
    def __str__(self):
        return self.zonamagazzino


class TblPercorso(models.Model):
    percorso_db = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_Percorso'


class TipoMacchina(models.Model):
    id_tipo_macchina = models.AutoField(primary_key=True)
    tipo_macchina = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_macchina'
        
    def __str__(self):
        return self.tipo_macchina
