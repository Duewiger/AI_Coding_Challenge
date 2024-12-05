# PDF Search Tool - Coding Challenge

Ein einfaches Tool zur Suche in PDF-Dokumenten unter Verwendung eines Language Models (LLM). Dieses Projekt ermöglicht es, Benutzeranfragen basierend auf PDF-Inhalten zu beantworten. Es wurde als Teil einer Coding Challenge entwickelt.

Gerne kann auch mittels Frontend im Browser mit der Anwendung interagiert und die Fragen gestellt werden.

=>
---
Für die Ausführung der Anwendung im Browser, einfach in den Folder 'optional_gui_chatbot' wechseln und der beigefügten README.md folgen
---

## Projektstruktur

```
coding_challenge
├── .venv/                 # Virtuelle Python-Umgebung
├── dataset_coding_challenge/
│   └── *.pdf              # PDF-Dokumente
├── .env                   # Umgebungsvariablen (z. B. OpenAI API Key)
├── .gitignore             # Dateien, die nicht in das Repo gehören
├── docker-compose.yml     # Docker Compose Konfiguration
├── Dockerfile             # Docker Image Konfiguration
├── main.py                # Hauptprogramm
└── README.md              # Diese Dokumentation
```

## Anforderungen
- Python 3.11
- OpenAI API-Schlüssel (Wichtig, API-Key wird temporär über Link bereitgestellt, siehe unten)

## Installation

### 1. Lokale Ausführung

1. **Repository klonen:**
   ```bash
   git clone https://github.com/Duewiger/coding_challenge.git
   cd coding_challenge
   ```

2. **Virtuelle Umgebung erstellen und aktivieren:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Für macOS/Linux
   .\.venv\Scripts\activate    # Für Windows
   ```

3. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen einrichten:**
   Erstelle eine `.env`-Datei mit folgendem Inhalt:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   #####
   Der API-Key wird über folgenden Link temporär von mir freigestellt: 

   https://send.bitwarden.com/#i3oqTVupIU6KjLIqAUAnpA/DaNaSUrwRWk9yeuiVnJ-kA
   #####

5. **Tool starten:**
   ```bash
   python main.py
   ```

---

### 2. Docker-Ausführung

1. **Umgebungsvariablen einrichten:**
   Erstelle eine `.env`-Datei mit folgendem Inhalt:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   #####
   Der API-Key wird über folgenden Link temporär von mir freigestellt: 

   https://send.bitwarden.com/#i3oqTVupIU6KjLIqAUAnpA/DaNaSUrwRWk9yeuiVnJ-kA
   #####

2. **Docker-Container erstellen und starten:**
   ```bash
   docker-compose up --build
   ```

3. **Mit dem Tool interagieren.**

   Sollte die main.py nicht direkt ausgeführt werden.

   Im Split-Terminal aufrufen:
   ```bash
   python main.py
   ```
---

## Verwendung

Nach dem Start des Programms kannst du Suchanfragen im Terminal eingeben. Beispielanfragen:

1. **Wie viel wiegt XBO 4000 W/HS XL OFR?**
2. **Welche Leuchte eignet sich am besten für mein Heimkino?**
3. **Gebe mir alle Leuchtmittel mit mindestens 1500W und einer Lebensdauer von mehr als 3000 Stunden.**
4. **Was ist die kleinste Einheit, die ich bestellen kann?**

Das Programm analysiert den Inhalt der PDFs und generiert Antworten basierend auf den Suchanfragen.

---

## Beispiel-Antworten

### Eingabe:
```
Wie viel wiegt XBO 4000 W/HS XL OFR?
```

### Ausgabe:
```
Die XBO 4000 W/HS XL OFR wiegt 1.022,90 g.
```

---

## Hinweise

- **Keine lokale Grafikkarte benötigt:** Alle Anfragen werden über die OpenAI-API verarbeitet.
- **Antwortzeit:** Das Tool liefert Antworten in wenigen Sekunden.
- **Erweiterbarkeit:** Weitere PDFs können einfach durch Hinzufügen in das Verzeichnis `dataset_coding_challenge` integriert werden.
  
