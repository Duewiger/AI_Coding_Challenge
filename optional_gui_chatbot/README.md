# Optional Chatbot Project mit Frontend

Ein einfaches Tool zur Suche in PDF-Dokumenten unter Verwendung eines Language Models (LLM). Dieses Projekt ermöglicht es, Benutzeranfragen basierend auf PDF-Inhalten zu beantworten. Es wurde als Teil einer Coding Challenge entwickelt.

## Anforderungen
- Python 3.11
- OpenAI API-Schlüssel (Wichtig, API-Key wird temporär über Link bereitgestellt, siehe unten)

# Chatbot mit PDF-Suche

Ein einfaches Tool zur Beantwortung von Fragen basierend auf zusätzlich hinzugefügten PDF-Inhalten.

## Schritte

1. Projekt erstellen und ins Verzeichnis wechseln
   ```bash
   git clone https://github.com/Duewiger/coding_challenge.git
   cd coding_challenge/optional_gui_chatbot
   ```

2. **Umgebungsvariablen einrichten:**
   Erstelle eine `.env`-Datei mit folgendem Inhalt:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   #####
   Der API-Key wird über folgenden Link temporär von mir freigestellt: 

   https://send.bitwarden.com/#i3oqTVupIU6KjLIqAUAnpA/DaNaSUrwRWk9yeuiVnJ-kA
   #####

3. Starte die Anwendung mit Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Öffne im Browser:

   http://127.0.0.1:8000


5. Die Weboberfläche ist nun vollständig einsatzbereit!


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

---

## Support

Falls Ihr Fragen habt ruft mich gerne auch einfach an: +49 (0) 172 - 745 27 73

Oder schreibt mir per mail unter: kd@duewiger.com