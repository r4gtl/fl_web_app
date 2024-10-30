# Usa l'immagine base di Python
FROM python:3.11-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt e installa le dipendenze
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia il file .env nel container
COPY .env /app/


# Copia il progetto Django all'interno del container
COPY . /app/
# Esegui le migrazioni
RUN python manage.py makemigrations && python manage.py migrate

# Espone la porta 8080 per il server web
EXPOSE 8080


# Comando per avviare Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "fl_web_app.wsgi:application"]
