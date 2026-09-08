# lekki obraz Pythona
FROM python:3.12-slim

# wyłączamy buforowanie wyjścia oraz zapobiegamy tworzeniu plików .pyc
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# kopiujemy listę zależności i je instalujemy
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# kopiujemy resztę kodu naszego projektu
COPY . .

# wystawiamy port, na którym będzie działać Django
EXPOSE 8000

# komenda odpalająca serwer API
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]